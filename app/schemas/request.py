# Models for requests (e.g., TaskRequest)
from pydantic import BaseModel, Field
from typing import Optional

class TaskRequest(BaseModel):
    """
    Request model for agent task execution.
    
    Attributes:
        session_id: Unique identifier for the user's session
        task: The user's query or command to be executed
    """
    session_id: str = Field(
        ..., 
        description="Unique identifier for the user's session",
        min_length=1,
        max_length=100,
        example="user_session_12345"
    )
    task: str = Field(
        ..., 
        description="The user's query or command to be executed",
        min_length=1,
        max_length=5000,
        example="What's the weather like in New York?"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "session_id": "user_session_12345",
                "task": "What's the weather like in New York?"
            }
        } 