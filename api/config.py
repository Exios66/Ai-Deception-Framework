from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AI Deception Framework"
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    LITERARY_VAULT_BASE_URL: str = "https://exios66.github.io/Literary-Vault/api/v1"
    
    # API Keys and Secrets
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    
    class Config:
        case_sensitive = True

settings = Settings() 