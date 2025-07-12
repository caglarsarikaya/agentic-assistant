import os
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    # API Configuration
    api_title: str = "Agentic Assistant API"
    api_version: str = "1.0.0"
    
    # LLM Configuration
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4"
    openai_temperature: float = 0.7
    
    # Database Configuration
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "agentic_assistant"
    
    # Search Configuration
    serper_api_key: Optional[str] = None
    
    # Google Calendar Configuration
    google_client_id: Optional[str] = None
    google_client_secret: Optional[str] = None
    google_redirect_uri: Optional[str] = None
    
    # Memory Configuration
    max_short_memory_size: int = 1000
    max_long_memory_size: int = 10000
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()

def get_settings() -> Settings:
    return settings 