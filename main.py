from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Study Backend",
        "done": False
    },
    {
        "id": 2,
        "title": "Go to Gym",
        "done": True
    },
    {
        "id": 3,
        "title": "Read FastAPI Docs",
        "done": False
    }
]

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{id}")
def update_task(id: int, updated_task: TaskUpdate):
    for task in tasks:
        if task["id"] == id:
            task["title"] = updated_task.title
            task["done"] = updated_task.done
            return task

    raise HTTPException(status_code=404, detail="Task not found")



@app.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Task not found")