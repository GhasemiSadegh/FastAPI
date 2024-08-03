from fastapi import FastAPI
from database import Library, Session, engine


app = FastAPI()


@app.post('/library')
def create_book(book: Library):
    with Session(engine) as session:
        session.add(book)
        session.commit()
    return 'Book added.'
