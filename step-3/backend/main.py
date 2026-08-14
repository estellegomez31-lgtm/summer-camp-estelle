import os
import random
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Field, Session, create_engine, select


# -----------------------------
# 🎯 Modèle : Task
# -----------------------------
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    done: bool = False


# -----------------------------
# 🎯 Base de données
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///familytask.db")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)

app = FastAPI(title="FamilyTask")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


def get_session():
    with Session(engine) as session:
        yield session


# -----------------------------
# 🎯 Titres aléatoires si titre vide
# -----------------------------
TITRES_ALEATOIRES = [
    "Ranger le salon",
    "Sortir les poubelles",
    "Arroser les plantes",
    "Passer l'aspirateur",
    "Faire la vaisselle",
    "Promener le chien",
]


# -----------------------------
# 🎯 Route : GET /api/tasks
# -----------------------------
@app.get("/api/tasks")
def list_tasks(session: Session = Depends(get_session)):
    return session.exec(select(Task)).all()


# -----------------------------
# 🎯 Route : POST /api/tasks
# Si titre vide → choisir un titre au hasard
# -----------------------------
@app.post("/api/tasks")
def add_task(title: str, session: Session = Depends(get_session)):
    if not title.strip():
        title = random.choice(TITRES_ALEATOIRES)

    task = Task(title=title)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


# -----------------------------
# 🎯 Route : PATCH /api/tasks/{id}
# Si tâche inexistante → erreur propre
# -----------------------------
@app.patch("/api/tasks/{id}")
def toggle_task(id: int, session: Session = Depends(get_session)):
    task = session.get(Task, id)

    if not task:
        raise HTTPException(status_code=404, detail=f"Tâche {id} introuvable")

    task.done = not task.done
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


# -----------------------------
# 🎯 Route : DELETE /api/tasks/{id}
# -----------------------------
@app.delete("/api/tasks/{id}")
def delete_task(id: int, session: Session = Depends(get_session)):
    task = session.get(Task, id)

    if not task:
        raise HTTPException(status_code=404, detail=f"Tâche {id} introuvable")

    session.delete(task)
    session.commit()
    return {"message": "Task deleted"}


# -----------------------------
# 🎯 Route de santé
# -----------------------------
@app.get("/api/health")
def health():
    return {"status": "ok"}