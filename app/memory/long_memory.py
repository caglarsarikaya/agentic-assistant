"""Stub for long-term memory using MongoDB.

This implementation falls back to in-memory storage if MongoDB is not
available. The goal is to keep the API surface simple for tests without
requiring a running database.
"""
from typing import List

try:
    from pymongo import MongoClient
    MONGO_AVAILABLE = True
except Exception:  # pragma: no cover - fallback when pymongo missing
    MONGO_AVAILABLE = False


class LongMemory:
    def __init__(self, uri: str, database: str):
        self._use_db = False
        self._store = {}
        if MONGO_AVAILABLE:
            try:
                client = MongoClient(uri, serverSelectionTimeoutMS=2000)
                client.server_info()  # Trigger connection
                self._collection = client[database]["memory"]
                self._use_db = True
            except Exception:
                self._use_db = False

    def add(self, session_id: str, message: str) -> None:
        if self._use_db:
            self._collection.insert_one({"session_id": session_id, "message": message})
        else:
            self._store.setdefault(session_id, []).append(message)

    def get(self, session_id: str) -> List[str]:
        if self._use_db:
            return [doc["message"] for doc in self._collection.find({"session_id": session_id})]
        return self._store.get(session_id, [])
