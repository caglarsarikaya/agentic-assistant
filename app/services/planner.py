"""Service that creates and exposes the PeerAgent."""
from typing import List

from app.agents.base import BaseAgent
from app.agents.peer_agent import PeerAgent
from app.agents.llm_agent import LLMAgent
from app.agents.search_agent import SearchAgent
from app.agents.calendar_agent import CalendarAgent
from app.agents.whatsapp_agent import WhatsAppAgent
from app.memory.short_memory import ShortMemory
from app.memory.long_memory import LongMemory
from app.core.config import settings


class PlannerService:
    def __init__(self) -> None:
        short = ShortMemory()
        long = LongMemory(settings.mongodb_uri, settings.mongodb_database)
        self.llm = LLMAgent(short, long)
        self.search = SearchAgent(short, long)
        self.calendar = CalendarAgent(short, long)
        self.whatsapp = WhatsAppAgent(short, long)
        # Register agents here. New agents can be added without modifying the
        # planner logic as long as they implement `can_handle`.
        agents: List[BaseAgent] = [self.llm, self.search, self.calendar, self.whatsapp]
        self.peer = PeerAgent(short, long, agents)

    def execute(self, session_id: str, task: str):
        return self.peer.execute(session_id, task)
