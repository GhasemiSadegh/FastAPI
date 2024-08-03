from fastapi import FastAPI
from sqlmodel import SQLModel, select
from models import BaseLibrary, engine
from database import Session


app = FastAPI()


@app.post('/library')
def create_book(book: BaseLibrary):
    with Session(engine) as session:
        session.add(book)
        session.commit()
    return 'Book added.'


@app.get('/books')
def show_books():
    with Session(engine) as session:
        selected = select(BaseLibrary)
        results = session.exec(selected)
        books = results.all()
        return (f'List of book \n'
                f'{books}')


@app.delete('/delete/{book_id}')
def delete_book(book_id: int):
    with Session(engine) as session:
        selected = session.exec(select(BaseLibrary).where(BaseLibrary.id == book_id)).first()
        session.delete(selected)
        session.commit()
        return f'The book with id {book_id} removed.'


@app.put('/update/{book_id}')
def update_book(book_id: int, new: BaseLibrary):
    with Session(engine) as session:
        selected = session.exec(select(BaseLibrary).where(BaseLibrary.id == book_id)).first()
        selected.title = new.title
        session.add(selected)
        session.commit()
        session.refresh(selected)
    return 'File Updated.'
