from fastapi import FastAPI, Body
from todo_model import Todo, TodoRequest
from datetime import datetime

app = FastAPI()

TODOS = [
    Todo(1, "title-1", "desc-1", False, 1),
    Todo(2, 'title-2', 'desc-2', True, 2)
]

@app.get("/todos/all")
async def get_all():
    return TODOS

@app.post('/todos/create_todo')
async def create_todo(todo: TodoRequest):
    t = Todo(**dict())
    print(t)

    return todo
