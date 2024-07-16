from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def hello():
    return 'hello'


@app.get('/log_in')
def log_in():
    return 'It is a log in page'


@app.get('/blogs/{name}')
def blog_name(name: int):
    return {'message': f'The name is {name}'}


