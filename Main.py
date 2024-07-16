from fastapi import FastAPI
from enum import Enum

# import uvicorn

app = FastAPI()


@app.get('/')
def hello():
    return 'hello'


@app.get('/log-in')
def log_in():
    return 'It is a log in page'


@app.get('/blogs/{name}')
def blog_name(name: int):
    return {'message': f'The name is {name}'}


class Limiter(str, Enum):
    Mesal1 = 'One'
    Mesal2 = 'Two'


@app.get('/test/{data}')
def test_data(data: Limiter):
    return {'message': f' The massage is {data}'}



