from fastapi import FastAPI
# from enum import Enum
# from typing import Optional
# import uvicorn
from BasicsPersian.router import practice, myhome_get, myhome_post

app = FastAPI()

app.include_router(myhome_get.router)
app.include_router(myhome_post.router)
app.include_router(practice.router)


@app.get('/')
def home_page():
    return 'This the home page with no endpoint'
