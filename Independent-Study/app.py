import os
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum

from fastapi import FastAPI, HTTPException, Depends, Security, status, Query, Body
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
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# FastAPI app setup
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
        # Log the error here
        print(f"Caught exception: {str(e)}")
        return JSONResponse(content={"error": "Internal server error"}, status_code=500)

# Middleware
app.add_middleware(HTTPSRedirectMiddleware)

# FastAPI app setup (moved from above)
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
        # Log the error here
        print(f"Caught exception: {str(e)}")
        return JSONResponse(content={"error": "Internal server error"}, status_code=500)

    title="Questions API",
    description="API for managing questions and answers",
    version="1.0.0",
# Remove this closing parenthesis as it's not needed and causing the "Expected expression" error

# FastAPI app setup
app = FastAPI(
    title="Questions API",
    description="API for managing questions and answers",
    version="1.0.0",
)

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
        return QuestionResponse(
            id=db_question.id,
            question=db_question.question,
            choices=[db_question.choice1, db_question.choice2, db_question.choice3, db_question.choice4],
            correct_answer=db_question.correct_answer,
            difficulty=db_question.difficulty,
            created_at=db_question.created_at,
            updated_at=db_question.updated_at
        )
    except Exception as e:
        logger.error(f"Error creating question: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create question")

@app.get("/questions/", response_model=List[QuestionResponse])
async def get_questions(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    difficulty: Optional[QuestionDifficulty] = None,
    db: Session = Depends(get_db)
):
    try:
        query = db.query(Question)
        if difficulty:
            query = query.filter(Question.difficulty == difficulty)
        questions = query.offset(skip).limit(limit).all()
        return [
            QuestionResponse(
                id=q.id,
                question=q.question,
                choices=[q.choice1, q.choice2, q.choice3, q.choice4],
                correct_answer=q.correct_answer,
                difficulty=q.difficulty,
                created_at=q.created_at,
                updated_at=q.updated_at
            )
            for q in questions
        ]
    except Exception as e:
        logger.error(f"Error fetching questions: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch questions")

@app.get("/questions/{question_id}", response_model=QuestionResponse)
async def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return QuestionResponse(
        id=question.id,
        question=question.question,
        choices=[question.choice1, question.choice2, question.choice3, question.choice4],
        correct_answer=question.correct_answer,
        difficulty=question.difficulty,
        created_at=question.created_at,
        updated_at=question.updated_at
    )

@app.put("/questions/{question_id}", response_model=QuestionResponse)
async def update_question(
    question_id: int,
    question_update: QuestionCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(verify_token)
):
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    try:
        db_question.question = question_update.question
        db_question.choice1 = question_update.choices[0]
        db_question.choice2 = question_update.choices[1]
        db_question.choice3 = question_update.choices[2]
        db_question.choice4 = question_update.choices[3]
        db_question.correct_answer = question_update.correct_answer
        db_question.difficulty = question_update.difficulty
        db_question.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(db_question)
        return QuestionResponse(
            id=db_question.id,
            question=db_question.question,
            choices=[db_question.choice1, db_question.choice2, db_question.choice3, db_question.choice4],
            correct_answer=db_question.correct_answer,
            difficulty=db_question.difficulty,
            created_at=db_question.created_at,
            updated_at=db_question.updated_at
        )
    except Exception as e:
        logger.error(f"Error updating question: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update question")

@app.delete("/questions/{question_id}")
async def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(verify_token)
):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    try:
        db.delete(question)
        db.commit()
        return JSONResponse(content={"message": "Question deleted successfully"})
    except Exception as e:
        logger.error(f"Error deleting question: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete question")

@app.post("/import-from-github")
async def import_from_github(
    owner: str,
    repo: str,
    file_path: str,
    db: Session = Depends(get_db),
    _: dict = Depends(verify_token)
):
    try:
        content = await fetch_file_from_github(owner, repo, file_path)
        questions = parse_github_content(content)
        
        for q in questions:
            db_question = Question(
                question=q["question"],
                choice1=q["choices"][0],
                choice2=q["choices"][1],
                choice3=q["choices"][2],
                choice4=q["choices"][3],
                correct_answer=q["correct_answer"],
                difficulty=q["difficulty"]
            )
            db.add(db_question)
        
        db.commit()
        return JSONResponse(content={"message": f"Successfully imported {len(questions)} questions"})
    except Exception as e:
        logger.error(f"Error importing questions from GitHub: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to import questions from GitHub")

def parse_github_content(content: str) -> List[Dict[str, Any]]:
    questions = []
    lines = content.strip().split("\n")
    current_question = {}
    
    for line in lines:
        if line.startswith("Q:"):
            if current_question:
                questions.append(current_question)
            current_question = {
                "question": line[2:].strip(),
                "choices": [],
                "correct_answer": None,
                "difficulty": QuestionDifficulty.MEDIUM  # Default difficulty
            }
        elif line.startswith("A:"):
            current_question["choices"].append(line[2:].strip())
        elif line.startswith("Correct:"):
            current_question["correct_answer"] = int(line[8:].strip())
        elif line.startswith("Difficulty:"):
            current_question["difficulty"] = QuestionDifficulty(line[11:].strip().lower())
    
    if current_question:
        questions.append(current_question)
    
    return questions

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        ssl_keyfile=None,
        ssl_certfile=None,
        log_level="debug"  # Add this line
    )
