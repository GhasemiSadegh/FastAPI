from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
import uvicorn
from router import myhome_get

app = FastAPI()

app.include_router(myhome_get.router)


@app.get('/')
def home_page():
    return 'This the home page with no endpoint'
