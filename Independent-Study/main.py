import os
import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from dotenv import load_dotenv
import httpx
import base64
import sqlite3
from typing import List, Dict, Any
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()

# Enable HTTPS
app.add_middleware(HTTPSRedirectMiddleware)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

@lru_cache()
def get_db_connection():
    return sqlite3.connect("questions.db")

async def fetch_file_from_github(owner: str, repo: str, file_path: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="File or repository not found")
    elif response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch file from GitHub")
    
    content = response.json()["content"]
    decoded_content = base64.b64decode(content).decode("utf-8")
    return decoded_content

def parse_questions(content: str) -> List[Dict[str, Any]]:
    questions = []
    lines = content.strip().split("\n")
    for i in range(0, len(lines), 4):
        question = {
            "id": int(lines[i]),
            "question": lines[i+1],
            "choices": lines[i+2].split("|")
        }
        questions.append(question)
    return questions

def fetch_questions_from_db(db: sqlite3.Connection) -> List[Dict[str, Any]]:
    try:
        cursor = db.cursor()
        cursor.execute("SELECT id, question, choice1, choice2, choice3, choice4 FROM questions")
        rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "question": row[1],
                "choices": row[2:]
            }
            for row in rows
        ]
    except sqlite3.Error as e:
        logger.error(f"SQLite error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")

@app.get("/fetch-questions")
async def fetch_questions(owner: str, repo: str, file_path: str):
    try:
        decoded_content = await fetch_file_from_github(owner, repo, file_path)
        questions = parse_questions(decoded_content)
        return {
            "content": "File successfully read and parsed",
            "questions": questions
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.get("/fetch-local-questions")
async def fetch_local_questions(db: sqlite3.Connection = Depends(get_db_connection)):
    try:
        questions = fetch_questions_from_db(db)
        return {
            "content": "Database successfully queried",
            "questions": questions
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}, exc.status_code

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")
