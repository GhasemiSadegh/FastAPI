from fastapi import APIRouter
from fastapi import FastAPI, status, Response
# from enum import Enum
from typing import Optional


router = APIRouter(prefix='/myhome', tags=['myhome'])


@router.get('', summary='Home page.',
            description='We are learning FastAPI and this is an example description.'
            )
def home():
    return 'home page'


@router.get('/pageone/{name}/{age}')
def my_details(name: str, age: int, postcode: Optional[str] = None, validity: bool = True):
    return {'name': f'{name}',
            'age': f'{age}',
            'postcode': f'{postcode}',
            'validity': f'{validity}'
            }


@router.get('/pagetwo', status_code=status.HTTP_200_OK, response_description='This is related to 200 ok')
def my_status(ids: int, response: Response):
    """
    - **ids**: This is where I can explain what ids is
    """
    if ids > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return 'id too big'
    return 'id is ok'


@router.get('/pagethree', tags=['Practice'], response_description='It is a response description.')
def to_repeat():
    """
    **This is also a description written in the method.**
    """
    return "ok"
