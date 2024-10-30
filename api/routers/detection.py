from fastapi import APIRouter, HTTPException
from ..models import DeceptionDetectionRequest, DeceptionDetectionResponse, Question
from ..services.deception_detector import DeceptionDetector
import logging
from typing import List

router = APIRouter()
logger = logging.getLogger(__name__)
detector = DeceptionDetector()

@router.post("/analyze", response_model=DeceptionDetectionResponse)
async def detect_deception(request: DeceptionDetectionRequest):
    """
    Analyze content for potential deception
    """
    try:
        result = await detector.analyze(request.content, request.context)
        return result
    except Exception as e:
        logger.error(f"Error detecting deception: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-questions", response_model=List[DeceptionDetectionResponse])
async def analyze_questions(questions: List[Question]):
    """
    Analyze a set of questions for potential deception
    """
    try:
        results = await detector.analyze_question_set(questions)
        return results
    except Exception as e:
        logger.error(f"Error analyzing questions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 