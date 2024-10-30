from fastapi import APIRouter, HTTPException
from ..models import QuestionRequest, RandomizeRequest, Question
from ..services.literary_vault_client import LiteraryVaultClient
from typing import List
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
client = LiteraryVaultClient()

@router.get("/questions/{category}", response_model=List[Question])
async def get_questions(
    category: str,
    limit: int = 10,
    random: bool = True
):
    """
    Get questions from Literary Vault
    """
    try:
        questions = await client.get_questions(category, limit, random)
        return questions
    except Exception as e:
        logger.error(f"Error getting questions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/questions/randomize", response_model=List[Question])
async def randomize_questions(request: RandomizeRequest):
    """
    Get randomized questions from Literary Vault
    """
    try:
        questions = await client.randomize_questions(
            request.category,
            request.count,
            request.seed
        )
        return questions
    except Exception as e:
        logger.error(f"Error randomizing questions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 