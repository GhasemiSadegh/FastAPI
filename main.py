from fastapi import FastAPI
from sqlmodel import SQLModel, select
from models import BaseLibrary
from database import engine, get_session


app = FastAPI()


@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post('/library')
def create_book(book: BaseLibrary):
    with get_session() as session:
        session.add(book)
        session.commit()
    return 'Book added.'


@app.get('/books')
def show_books():
    with get_session() as session:
        selected = select(BaseLibrary)
        results = session.exec(selected)
        books = results.all()
        return (f'List of books: \n'
                f'{books}')


@app.delete('/delete/{book_id}')
def delete_book(book_id: int):
    with get_session() as session:
        selected = session.exec(select(BaseLibrary).where(BaseLibrary.id == book_id)).first()
        session.delete(selected)
        session.commit()
        return f'The book with id {book_id} is removed.'


@app.put('/update/{book_id}')
def update_book(book_id: int, new: BaseLibrary):
    with get_session() as session:
        selected = session.exec(select(BaseLibrary).where(BaseLibrary.id == book_id)).first()
        selected.title = new.title
        session.add(selected)
        session.commit()
        session.refresh(selected)
    return 'File Updated.'
