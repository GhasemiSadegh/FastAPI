from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()


class GenreURLChoices(Enum):
    ROCK = 'rock'
    JAZZ = 'jazz'
    HIPHOP = 'hip hop'
    POP = 'pop'


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


@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='band not found')
    return band


# @app.get('/bands/genre/{genre}')
# async def bands_for_genre(genre: str) -> list[dict]:
#     return [b for b in BANDS if genre.lower() == b['genre'].lower()]


@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [b for b in BANDS if genre.value == b['genre'].lower()]

