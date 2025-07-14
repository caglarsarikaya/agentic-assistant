from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List, Union
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    """Enumeration of task execution statuses."""
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"

class ErrorCode(str, Enum):
    """Standardized error codes for consistent error handling."""
    VALIDATION_ERROR = "validation_error"
    API_ERROR = "api_error"
    AUTHENTICATION_ERROR = "authentication_error"
    NOT_FOUND_ERROR = "not_found_error"
    TIMEOUT_ERROR = "timeout_error"

class TaskResponse(BaseModel):
    """Response model for agent task execution."""
    status: TaskStatus = Field(
        ...,
        description="Status of the task execution.",
        example=TaskStatus.SUCCESS
    )
    agent_types: List[str] = Field(
        ...,
        description="List of agent types that processed the task (e.g., 'llm', 'search', 'calendar').",
        min_items=1,
        example=["peer", "search", "calendar"]
    )
    result: Union[str, Dict[str, Any]] = Field(
        ...,
        description="The main result or response from the agent (string or structured data).",
        example="The weather in Paris is 20°C and sunny."
    )
    session_id: str = Field(
        ...,
        description="Session identifier for the request.",
        example="user_session_12345"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the response was generated."
    )
    error_message: Optional[str] = Field(
        None,
        description="Error message if the task failed.",
        example="Failed to access calendar API."
    )
    sub_tasks: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="Details of sub-tasks for multi-agent workflows.",
        example=[
            {"step": 1, "action": "search", "result": "Found showtime: 2025-07-15T19:00"},
            {"step": 2, "action": "calendar", "result": "Event created: abc123"}
        ]
    )

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "agent_types": ["peer", "search", "calendar"],
                "result": {"showtime": "2025-07-15T19:00:00", "event_id": "abc123"},
                "session_id": "user_session_12345",
                "timestamp": "2025-07-13T21:18:00Z",
                "error_message": None,
                "sub_tasks": [
                    {"step": 1, "action": "search", "result": "Found showtime: 2025-07-15T19:00"},
                    {"step": 2, "action": "calendar", "result": "Event created: abc123"}
                ]
            }
        }

class ErrorResponse(BaseModel):
    """Standard error response model."""
    status: TaskStatus = Field(
        default=TaskStatus.FAILED,
        description="Status of the error response, always 'failed'.",
        example=TaskStatus.FAILED
    )
    error_code: ErrorCode = Field(
        ...,
        description="Machine-readable error code.",
        example=ErrorCode.VALIDATION_ERROR
    )
    error_message: str = Field(
        ...,
        description="Human-readable error message.",
        example="Invalid session ID provided."
    )
    details: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional error details.",
        example={"field": "session_id", "value": "", "constraint": "non_empty"}
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the error occurred."
    )

    class Config:
        schema_extra = {
            "example": {
                "status": "failed",
                "error_code": "validation_error",
                "error_message": "Invalid session ID provided.",
                "details": {"field": "session_id", "value": "", "constraint": "non_empty"},
                "timestamp": "2025-07-13T21:18:00Z"
            }
        }