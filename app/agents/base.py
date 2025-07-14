"""Base class for all agents."""
from abc import ABC, abstractmethod
from typing import Any

from app.memory.short_memory import ShortMemory
from app.memory.long_memory import LongMemory


class BaseAgent(ABC):
    def __init__(self, name: str, description: str,
                 short_memory: ShortMemory, long_memory: LongMemory):
        self.name = name
        self.description = description
        self.short_memory = short_memory
        self.long_memory = long_memory

    def log(self, session_id: str, message: str) -> None:
        """Store a message in both short and long memory."""
        self.short_memory.add(session_id, message)
        self.long_memory.add(session_id, message)

    @abstractmethod
    def can_handle(self, task: str) -> bool:
        """Return True if this agent should handle the task."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, session_id: str, task: str) -> Any:
        """Execute the task and return a result."""
        raise NotImplementedError
