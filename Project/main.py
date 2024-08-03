from fastapi import FastAPI
from database import Library, Session, engine
from sqlmodel import SQLModel, select

app = FastAPI()


@app.post('/library')
def create_book(book: Library):
    with Session(engine) as session:
        session.add(book)
        session.commit()
    return 'Book added.'


@app.get('/books')
def show_books():
    with Session(engine) as session:
        selected = select(Library)
        results = session.exec(selected)
        books = results.all()
        return (f'List of book \n'
                f'{books}')


@app.delete('/delete/{book_id}')
def delete_book(book_id: int):
    with Session(engine) as session:
        selected = session.exec(select(Library).where(Library.id ==book_id)).first()
        session.delete(selected)
        session.commit()
        return f'The book with id {book_id} removed.'


