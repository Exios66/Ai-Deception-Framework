from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class ModelType(str, Enum):
    NEURAL_NETWORK = "neural_network"
    TRANSFORMER = "transformer"
    DECISION_TREE = "decision_tree"
    OTHER = "other"

class AnalysisRequest(BaseModel):
    model_data: bytes = Field(..., description="Binary model data")
    model_type: ModelType
    description: Optional[str] = None

class AnalysisResponse(BaseModel):
    model_type: ModelType
    accuracy: float
    deception_points: List[str]
    recommendation: str
    confidence_score: float

class DeceptionDetectionRequest(BaseModel):
    content: str = Field(..., min_length=1, max_length=10000)
    context: Optional[str] = None

class DeceptionDetectionResponse(BaseModel):
    probability: float
    confidence: float
    issues: List[str]
    recommendations: List[str]

class Category(str, Enum):
    ASTRONOMY = "astronomy"
    LITERATURE = "literature"
    MATHEMATICS = "mathematics"

class Question(BaseModel):
    id: str
    question: str
    correct_answer: str
    options: Optional[List[str]] = None

class QuestionRequest(BaseModel):
    category: Category
    limit: Optional[int] = Field(10, ge=1, le=50)
    random: Optional[bool] = True

class RandomizeRequest(BaseModel):
    category: Category
    count: Optional[int] = Field(5, ge=1, le=20)
    seed: Optional[int] = None 