from fastapi import FastAPI, APIRouter, Body, Query
from pydantic import BaseModel
from typing import Optional, List

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
                                          max_length=10,
                                          min_length=2
                                          )
                 ):
    return {
        'data': 'ok',
        'question_id': question_id}


@router.post('/users/accounts/{id}')
def meta_data(content: str, number: int, acc_id=Query(0,
                                                      max_length=10,
                                                      min_length=4,
                                                      alias='User Account ID',
                                                      description='Practicing meta data for a Query')):
    return {'content': content,
            'ID': acc_id,
            'number': number}


@router.post('/list-strings')
def list_str(first_par: list[str] = Query(),  second_par: Optional[List[int]] = Query(None)):
    return {'msg': f'Your strings are {first_par} and your integers are {second_par}'}
