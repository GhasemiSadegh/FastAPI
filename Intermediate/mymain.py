from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from models import GenreURLChoices, BandBase, BandCreate, Band, Album
from typing import Annotated
from contextlib import asynccontextmanager
from db import init_db, get_session
from sqlmodel import Session, select


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get('/bands')
async def bands(
        genre: GenreURLChoices | None = None,
        q: Annotated[str | None, Query(max_length=10)] = None,
        session: Session = Depends(get_session)
) -> list[Band]:

    band_list = session.exec(select(Band)).all()
    if q:
        band_list = [b for b in band_list if q.lower() in b.name.lower()
                     ]
    if genre:
        band_list = [b for b in band_list if genre.value == b.genre.lower()
                     ]
    return band_list


@app.get('/bands/{band_id}')
async def band(
        band_id: Annotated[int, Path(title="Band ID", description='This is description')],
        session : Session = Depends(get_session)
) -> Band:
    band = session.get(Band, band_id)
    if band is None:
        raise HTTPException(status_code=404, detail='band not found')
    return band
#
#
# # @app.get('/bands/genre/{genre}')
# # async def bands_for_genre(genre: str) -> list[dict]:
# #     return [b for b in BANDS if genre.lower() == b['genre'].lower()]
#
#
# @app.get('/bands/genre/{genre}')
# async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
#     return [b for b in BANDS if genre.value == b['genre'].lower()]
#
#


@app.post('/bands')
async def create_band(
        band_data: BandCreate,
        session: Session = Depends(get_session)
) -> Band:
    band = Band(name=band_data.name, genre=band_data.genre)
    session.add(band)
    if band_data.albums:
        for album in band_data.albums:
            album_obj = Album(title=album.title, release_date=album.release_date, band=band)
            session.add(album_obj)
    session.commit()
    session.refresh(band)
    return band
