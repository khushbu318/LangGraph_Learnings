from fastapi import FastAPI

app = FastAPI()

TODOS = [
    {'title':'title1','desc':'desc1','is_completed':False},
    {'title':'title2','desc':'desc2','is_completed':False},
    {'title':'title3','desc':'desc3','is_completed':False}
]

@app.get("/")
def hello_world():
    return 'Hi winner'


@app.get("/todos/all")
def get_all_todos():
    return TODOS

