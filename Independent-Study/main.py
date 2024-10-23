import os
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum

from fastapi import FastAPI, HTTPException, Depends, Request, Security, status, Query, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import httpx
import base64
import jwt
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
class Config:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///questions.db")
    JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

# Database setup
Base = declarative_base()

class QuestionDifficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    choice1 = Column(String(255), nullable=False)
    choice2 = Column(String(255), nullable=False)
    choice3 = Column(String(255), nullable=False)
    choice4 = Column(String(255), nullable=False)
    correct_answer = Column(Integer, nullable=False)
    difficulty = Column(SQLEnum(QuestionDifficulty), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Pydantic models
class QuestionBase(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000)
    choices: List[str] = Field(..., min_items=4, max_items=4)
    correct_answer: int = Field(..., ge=1, le=4)
    difficulty: QuestionDifficulty

    class Config:
        orm_mode = True

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    created_at: datetime
    updated_at: datetime

class ErrorResponse(BaseModel):
    detail: str

# Database connection
engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app setup
app = FastAPI(
    title="Questions API",
    description="API for managing questions and answers",
    version="1.0.0",
)

@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Caught exception: {str(e)}")
        return JSONResponse(content={"error": "Internal server error"}, status_code=500)

# Middleware
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        payload = jwt.decode(credentials.credentials, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

# GitHub integration
async def fetch_file_from_github(owner: str, repo: str, file_path: str) -> str:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization": f"token {Config.GITHUB_TOKEN}"}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
        except httpx.HTTPError as e:
            logger.error(f"GitHub API error: {str(e)}")
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="File or repository not found")
            raise HTTPException(status_code=500, detail="Failed to fetch file from GitHub")
    
    content = response.json()["content"]
    return base64.b64decode(content).decode("utf-8")

# Routes
@app.post("/questions/", response_model=QuestionResponse)
async def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(verify_token)
):
    try:
        db_question = Question(
            question=question.question,
            choice1=question.choices[0],
            choice2=question.choices[1],
            choice3=question.choices[2],
            choice4=question.choices[3],
            correct_answer=question.correct_answer,
            difficulty=question.difficulty
        )
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question
    except Exception as e:
        logger.error(f"Error creating question: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create question")

@app.get("/questions/", response_model=List[QuestionResponse])
async def get_questions(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    difficulty: Optional[QuestionDifficulty] = None
):
    query = db.query(Question)
    if difficulty:
        query = query.filter(Question.difficulty == difficulty)
    questions = query.offset(skip).limit(limit).all()
    return questions

@app.get("/questions/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.put("/questions/{question_id}", response_model=QuestionResponse)
async def update_question(
    question_id: int,
    question_update: QuestionCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(verify_token)
):
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    
    for key, value in question_update.dict().items():
        setattr(db_question, key, value)
    
    db.commit()
    db.refresh(db_question)
    return db_question

@app.delete("/questions/{question_id}", response_model=dict)
async def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(verify_token)
):
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db.delete(db_question)
    db.commit()
    return {"message": "Question deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")
