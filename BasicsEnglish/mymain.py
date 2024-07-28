from fastapi import FastAPI, HTTPException, Path, Query, Body
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID
from typing import Annotated

app = FastAPI()


@app.get('/')
async def index():
    return {'message': "Hello World"}


@app.get('/about')
async def about() -> str:
    return 'An amazing company'


BANDS = [
    {'id': 1, 'name': 'Ali', 'genre': 'Rock',
     'albums': [
         {'title': 'Flowers of Spring', 'release_date': '2023-01-02'}
     ]
     },
    {'id': 2, 'name': 'Reza', 'genre': 'Jazz'},
    {'id': 3, 'name': 'Gholam', 'genre': 'Hip Hop',
     'albums': [
         {'title': 'Master of Reality', 'release_date': '2024-01-01'}
     ]
     },
    {'id': 4, 'name': 'Feri', 'genre': 'Pop'}
]


@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None,
                q: Annotated[str | None, Query(max_length=10)] = None) -> list[BandWithID]:
    band_list = [BandWithID(**b) for b in BANDS]  # ** unpacks the values of each item in the dict

    if q:
        band_list = [b for b in band_list if q.lower() in b.name.lower()
                     ]
    if genre:
        band_list = [b for b in band_list if genre.value == b.genre.lower()
                     ]
    # if has_album:
    #     band_list = [b for b in band_list if len(b.albums) > 0]

    return band_list


@app.get('/bands/{band_id}')
async def band(band_id: Annotated[int, Path(title="Band ID", description='This is description')]) -> BandWithID:
    band = next((BandWithID(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='band not found')
    return band


# @app.get('/bands/genre/{genre}')
# async def bands_for_genre(genre: str) -> list[dict]:
#     return [b for b in BANDS if genre.lower() == b['genre'].lower()]


@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [b for b in BANDS if genre.value == b['genre'].lower()]


@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1  # it will give us a 5 in this example
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band

# using postman to test the post and get requests
# installed SQLModel
