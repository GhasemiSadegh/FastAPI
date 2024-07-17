from fastapi import FastAPI
from enum import Enum

# import uvicorn

app = FastAPI()


@app.get('/')
def hello():
    return 'home page nothing after slash'


@app.get('/log-in')
def log_in():
    return 'using log in method with a get'


@app.get('/blogs/{name}')
def blog_name(name: int):
    return {'message': f'{name} is taken from user after blogs'}


class Limiter(str, Enum):
    Mesal1 = 'One'
    Mesal2 = 'Two'


@app.get('/queries')
def test_query(name: str = None, age: int = None):
    return {'message': f'{name=} -- {age=}'}


