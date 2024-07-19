from fastapi import FastAPI, APIRouter, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/my-library', tags=['Books'])


class SearchValidator(BaseModel):
    author: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = 1
    name: Optional[str] = None


@router.get('/books/{book_id}')  # book_id is embedded in the link where the book photo is
def photos(book_id):
    if book_id:
        return 'Available'
    return 'Not available'


@router.post('/books/search')
def search(onesearch: SearchValidator):
    return {'author': onesearch.author}


@router.post('/books')
def body_parameter(content: str = Body(..., min_length=10, max_length=15, regex='^[A-Z].*')):
    return content

