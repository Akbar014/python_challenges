

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {'data': 'world'}

@app.get("/abc")
def abc():
    return {'data': [1,2,3]}

