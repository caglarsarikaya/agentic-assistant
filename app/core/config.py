import os
from typing import Optional
from pydantic import BaseSettings, Field, validator
from pathlib import Path

class Settings(BaseSettings):
    # API Configuration
    api_title: str = Field(default="Agentic Assistant API", env="API_TITLE")
    api_version: str = Field(default="1.0.0", env="API_VERSION")
    debug: bool = Field(default=False, env="DEBUG")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    
    # LLM Configuration
    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4", env="OPENAI_MODEL")
    openai_temperature: float = Field(default=0.7, env="OPENAI_TEMPERATURE")
    
    # Database Configuration
    mongodb_uri: str = Field(default="mongodb://localhost:27017", env="MONGODB_URI")
    mongodb_database: str = Field(default="agentic_assistant", env="MONGODB_DATABASE")
    
    # Search Configuration
    serper_api_key: Optional[str] = Field(default=None, env="SERPER_API_KEY")
    
    # Google Calendar Configuration
    google_client_id: Optional[str] = Field(default=None, env="GOOGLE_CLIENT_ID")
    google_client_secret: Optional[str] = Field(default=None, env="GOOGLE_CLIENT_SECRET")
    google_redirect_uri: Optional[str] = Field(default=None, env="GOOGLE_REDIRECT_URI")
    
    # Memory Configuration
    max_short_memory_size: int = Field(default=1000, env="MAX_SHORT_MEMORY_SIZE")
    max_long_memory_size: int = Field(default=10000, env="MAX_LONG_MEMORY_SIZE")
    
    @validator('openai_api_key')
    def validate_openai_api_key(cls, v):
        if v is None:
            raise ValueError("OPENAI_API_KEY is required")
        return v
    
    @validator('openai_model')
    def validate_openai_model(cls, v):
        valid_models = ['gpt-4', 'gpt-4-turbo', 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k']
        if v not in valid_models:
            raise ValueError(f"Invalid OpenAI model. Must be one of: {valid_models}")
        return v
    
    @validator('openai_temperature')
    def validate_temperature(cls, v):
        if not 0 <= v <= 2:
            raise ValueError("Temperature must be between 0 and 2")
        return v
    
    @validator('log_level')
    def validate_log_level(cls, v):
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if v.upper() not in valid_levels:
            raise ValueError(f"Invalid log level. Must be one of: {valid_levels}")
        return v.upper()
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # Allow environment variables to override .env file
        env_ignore_empty = True

# Global settings instance
settings = Settings()

def get_settings() -> Settings:
    """Get the global settings instance."""
    return settings

def validate_settings() -> bool:
    """Validate that all required settings are properly configured."""
    try:
        # This will trigger validation
        _ = settings.openai_api_key
        return True
    except ValueError as e:
        print(f"Configuration error: {e}")
        return False

def get_env_file_path() -> Path:
    """Get the path to the .env file."""
    return Path(".env")

def is_env_file_exists() -> bool:
    """Check if .env file exists."""
    return get_env_file_path().exists() 