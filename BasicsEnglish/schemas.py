from enum import Enum
from pydantic import BaseModel
from datetime import date


class Album(BaseModel):
    title: str
    release_date: date


class BandBase(BaseModel):
    name: str
    genre: str
    albums: list[Album] = []


class BandCreate(BandBase):
    pass


class BandWithID(BandBase):
    id: int


class GenreURLChoices(Enum):
    ROCK = 'rock'
    JAZZ = 'jazz'
    HIPHOP = 'hip hop'
    POP = 'pop'
