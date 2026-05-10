import os
from dotenv import load_dotenv
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    
    # Github settings
    GITHUB_REPO_URL: str
    GITHUB_BRANCH: str
    
    # Application settings
    DEBUG: bool
    LOG_LEVEL: str
    
    class Config:
        env_file = ".env"

def load_config():
    """Load and validate configuration settings"""
    load_dotenv()
    return Settings()