from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {'message': "Hello World"}


@app.get('/about')
async def about() -> str:
    return 'An amazing company'

BANDS = [
    {'id': 1, 'name': 'Ali', 'genre': 'Rock'},
    {'id': 2, 'name': 'Reza', 'genre': 'Jazz'},
    {'id': 3, 'name': 'Gholam', 'genre': 'Hip Hop'},
    {'id': 4, 'name': 'Feri', 'genre': 'Pop'}
]


@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS


