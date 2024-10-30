from fastapi import APIRouter, HTTPException, UploadFile, File
from ..models import AnalysisRequest, AnalysisResponse, ModelType
from ..services.model_analyzer import ModelAnalyzer
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
model_analyzer = ModelAnalyzer()

@router.post("/model", response_model=AnalysisResponse)
async def analyze_model(file: UploadFile = File(...)):
    """
    Analyze an uploaded AI model for potential deception points
    """
    try:
        contents = await file.read()
        model_type = ModelType.OTHER  # Determine model type from file
        
        analysis_request = AnalysisRequest(
            model_data=contents,
            model_type=model_type
        )
        
        result = await model_analyzer.analyze(analysis_request)
        return result
    except Exception as e:
        logger.error(f"Error analyzing model: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 