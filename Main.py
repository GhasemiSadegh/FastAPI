from fastapi import FastAPI
from enum import Enum
from typing import Optional
import uvicorn

app = FastAPI()


@app.get('/home/{name}/{age}')
def home(name: str, age: int, postcode: Optional[str] = None, validity: bool = True):
    return {'name': f'{name}',
            'age': f'{age}',
            'postcode': f'{postcode}',
            'validity': f'{validity}'
            }
