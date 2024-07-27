from enum import Enum
from pydantic import BaseModel
from datetime import date


class Album(BaseModel):
    title: str
    release_date: date


class Band(BaseModel):
    id: int
    name: str
    genre: str
    albums: list[Album] = []





class GenreURLChoices(Enum):
    ROCK = 'rock'
    JAZZ = 'jazz'
    HIPHOP = 'hip hop'
    POP = 'pop'