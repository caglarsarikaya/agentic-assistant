"""API routes for agent execution."""
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.planner import PlannerService

router = APIRouter()
planner = PlannerService()


class TaskRequest(BaseModel):
    session_id: str
    task: str


@router.post("/agent/execute")
async def execute_task(request: TaskRequest):
    result = planner.execute(request.session_id, request.task)
    return {"result": result}
