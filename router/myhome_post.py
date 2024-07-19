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
