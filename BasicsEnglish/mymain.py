from fastapi import FastAPI, HTTPException

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


@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='band not found')
    return band
