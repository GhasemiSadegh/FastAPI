from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/myhome', tags=['posts'])


class PydanticValidator(BaseModel):
    name: str
    age: int
    postalcode: Optional[int] = None
    present: bool = True


@router.post('/users')
def my_users(data: PydanticValidator):
    return {'Msg': 'ok', "data": data} # this will go back to client/user = response body


@router.post('/users/details/{id}')
def my_details(data: PydanticValidator, id: int, version: int = 1):
    return {'msg': 'Your are registered.',
            'data': data,
            'Your id': id,
            'The version': version}


@router.post('/users/questions')
def my_questions(data: PydanticValidator, question_id: int = Query(None, title='text', description='text',
                                                                   alias='QuestionID', deprecated=False)):
    return {
        'data': data,
        'question_id': question_id
    }