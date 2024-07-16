from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def hello():
    return 'hello'


@app.get('/log_in')
def log_in():
    return 'It is a log in page'


@app.post('/log_in')
def log_in_two():
    return "It's the log in second page"

