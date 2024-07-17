from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
import uvicorn

app = FastAPI()


@app.get('/myhome', summary='Home page.', description='We are learning FastAPI and this is an example description.')
def home():
    return 'home page'


@app.get('/myhome/pageone/{name}/{age}', tags=['learning'])
def my_details(name: str, age: int, postcode: Optional[str] = None, validity: bool = True):
    return {'name': f'{name}',
            'age': f'{age}',
            'postcode': f'{postcode}',
            'validity': f'{validity}'
            }


@app.get('/myhome/pagetwo', status_code=status.HTTP_200_OK, tags=['learning'], response_description='This is related to 200 ok')
def my_status(ids: int, response: Response):
    """
    - **ids**: This is where I can explain what id is
    """
    if ids > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return 'id too big'
    return 'id is ok'


@app.get('/myhome/pagethree', tags=['Practice'], response_description='It is a response description.')
def to_repeat():
    """
    **This is also a description written in the method.**
    """
    return "ok"

