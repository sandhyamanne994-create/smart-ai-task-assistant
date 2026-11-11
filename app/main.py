from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.tools.task_tool import (
    create_task,
    get_tasks,
    complete_task,
    delete_task
)

app = FastAPI(
    title="Smart AI Task Assistant",
    description="My first AI Agent project",
    version="1.0.0"
)


class TaskRequest(BaseModel):
    task_name: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart AI Task Assistant!",
        "status": "Running Successfully"
    }


@app.get("/health")
def health():
    return {"status": "Healthy"}


@app.post("/tasks")
def add_task(request: TaskRequest):
    return create_task(request.task_name)


@app.get("/tasks")
def list_tasks():
    return get_tasks()


@app.patch("/tasks/{task_id}/complete")
def finish_task(task_id: int):
    result = complete_task(task_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail="Task not found")

    return result


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    result = delete_task(task_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail="Task not found")

    return result
