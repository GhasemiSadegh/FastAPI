from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import Optional


router = APIRouter(prefix='/my-library', tags=['Books'])


class SearchValidator(BaseModel):
    author: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    name: Optional[str] = None


@router.get('/books/{book_id}') # book_id is embedded in the link where the book photo is
def photos(book_id):
    if book_id:
        return 'Available'
    return 'Not available'


@router.post('/books/search')
def search(data: BaseModel, author, genre, year, name):
    return {'Search result is': data}

