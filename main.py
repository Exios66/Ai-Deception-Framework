import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import httpx
import base64
import json

load_dotenv()

app = FastAPI()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

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

def parse_questions(content: str):
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

@app.get("/fetch-questions")
async def fetch_questions(owner: str, repo: str, file_path: str):
    try:
        decoded_content = await fetch_file_from_github(owner, repo, file_path)
        questions = parse_questions(decoded_content)
        return {
            "decoded_content": decoded_content,
            "questions": questions
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
