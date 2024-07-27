from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band

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
    {'id': 3, 'name': 'Gholam', 'genre': 'Hip Hop',
     'albums': [
         {'title': 'Master of Reality', 'release_date': '2024-01-01'}
     ]
     },
    {'id': 4, 'name': 'Feri', 'genre': 'Pop'}
]


@app.get('/bands')
async def bands() -> list[Band]:
    return [
        Band(**b) for b in BANDS
    ]


@app.get('/bands/{band_id}')
async def band(band_id: int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='band not found')
    return band


# @app.get('/bands/genre/{genre}')
# async def bands_for_genre(genre: str) -> list[dict]:
#     return [b for b in BANDS if genre.lower() == b['genre'].lower()]


@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [b for b in BANDS if genre.value == b['genre'].lower()]
