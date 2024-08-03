from fastapi import FastAPI
from database import Library


app = FastAPI()


@app.post('/library')
def create_book(book: Library):
    return 'ok'