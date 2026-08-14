from fastapi.testclient import TestClient
from main import app

def test_inscription_puis_tache():
    client = TestClient(app)


    # 1. Inscription
    r = client.post("/api/signup", params={
        "email": "test@test.fr",
        "password": "abc",
        "name": "Test",
        "family": "FamTest"
    })
    assert r.status_code == 200
    token = r.json()["token"]

    # 2. Création d’une tâche
    r = client.post("/api/tasks", params={"title": "Ma tâche"},
                    headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200

    # 3. Vérification
    r = client.get("/api/tasks", headers={"Authorization": f"Bearer {token}"})
    tasks = r.json()
    assert any(t["title"] == "Ma tâche" for t in tasks)

def test_tasks_sans_token():
    client = TestClient(app)
    r = client.get("/api/tasks")
    assert r.status_code == 401