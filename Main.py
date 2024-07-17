from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
import uvicorn

app = FastAPI()


@app.get('/', summary='Home page.')
def home():
    return 'home page'


@app.get('/home/{name}/{age}', tags=['learning'])
def home(name: str, age: int, postcode: Optional[str] = None, validity: bool = True):
    return {'name': f'{name}',
            'age': f'{age}',
            'postcode': f'{postcode}',
            'validity': f'{validity}'
            }


@app.get('/stt', status_code=status.HTTP_200_OK, tags=['learning'])
def stt(ids: int, response: Response):
    if ids > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return 'id too big'
    return 'id is ok'
