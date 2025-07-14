"""Simple in-memory session storage."""
from collections import defaultdict
from typing import List

class ShortMemory:
    """Stores recent interactions for each session."""

    def __init__(self):
        self._store = defaultdict(list)

    def add(self, session_id: str, message: str) -> None:
        self._store[session_id].append(message)

    def get(self, session_id: str) -> List[str]:
        return self._store.get(session_id, [])

    def clear(self, session_id: str) -> None:
        if session_id in self._store:
            del self._store[session_id]
