from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_llm_question():
    resp = client.post("/v1/agent/execute", json={"session_id": "s1", "task": "how are you today?"})
    assert resp.status_code == 200
    assert "llm" in resp.json()["result"]


def test_simple_math():
    resp = client.post("/v1/agent/execute", json={"session_id": "s1", "task": "tell me what makes 3+5=?"})
    assert resp.status_code == 200
    assert resp.json()["result"]["llm"].lower().startswith("3 + 5")


def test_search_and_text():
    resp = client.post("/v1/agent/execute", json={"session_id": "s1", "task": "check weather at paris, then text it to my friend"})
    assert resp.status_code == 200
    data = resp.json()["result"]
    assert "search" in data and "whatsapp" in data


def test_search_calendar():
    task = "create an event for my calendar, check when pulp fiction plays at state theatre and create a event reminder for me"
    resp = client.post("/v1/agent/execute", json={"session_id": "s2", "task": task})
    assert resp.status_code == 200
    data = resp.json()["result"]
    assert "search" in data and "calendar" in data
