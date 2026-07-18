from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "name": "Learn Docker"},
    {"id": 2, "name": "Learn kubernetes"}
]

@app.get("/")
def home():
    return {
        "message": "Task Manager API running"
    }

@app.get("/tasks")
def get_tasks():
    return tasks    

@app.post("/tasks")
def add_task(task: dict):
    tasks.append(task)
    return task