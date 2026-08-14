import os
import sys

from fastapi.testclient import TestClient
from sqlmodel import SQLModel

sys.path.insert(0, os.path.dirname(__file__))
os.environ["DATABASE_URL"] = "sqlite:///test_familytask.db"

from main import app, engine


def test_task_crud_flow():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    client = TestClient(app)

    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.json() == []

    response = client.post("/api/tasks", params={"title": "Test task"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["title"] == "Test task"
    task_id = payload["id"]

    response = client.get("/api/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["id"] == task_id

    response = client.patch(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["done"] is True

    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["ok"] is True
