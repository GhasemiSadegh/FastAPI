from fastapi import FastAPI, APIRouter, Body, Query
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
def body_parameter(comment: str = Body(...,
                                       min_length=10,
                                       max_length=15,
                                       regex='^[A-Z].*'
                                       )
                   ):
    return comment


@router.post('/users/questions')
def my_questions(question_id: int = Query(None,
                                          title='text',
                                          description='text',
                                          alias='QuestionID',
                                          deprecated=False,
                                          max_length=5,
                                          min_length=20
                                          )
                 ):
    return {
        'data': 'ok',
        'question_id': question_id}


@router.post('/users/accounts')
def meta_data(acc_id: int = Query(0, max_length=)):
