from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_all_tasks,get_task_by_id,create_task,update_task,delete_task

app = FastAPI()


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
    return get_all_tasks()

@app.get("/tasks/{id}")
def get_task(id: int):
    task = get_task_by_id(id)

    if task is None:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})

    return task

@app.post("/tasks", status_code=201)
def add_task(task_data: TaskCreate):
    # Validation: Ensure title is not empty
    if not task_data.title.strip():
        raise HTTPException(status_code=400, detail={"error": "Title is required"})
    
    return create_task(task_data.title)

@app.put("/tasks/{id}")
def update_task_endpoint(id: int, updated_task: TaskUpdate):
    task = update_task(
        id,
        updated_task.title,
        updated_task.done
    )

    if task is None:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})

    return task



@app.delete("/tasks/{id}", status_code=204)
def delete_task_endpoint(id: int):
    deleted = delete_task(id)

    if not deleted:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})