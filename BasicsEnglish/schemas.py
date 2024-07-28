from enum import Enum
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import date


class AlbumBase(SQLModel):
    title: str
    release_date: date


class Album(AlbumBase, table=True):
    id: int = Field(default=None, primary_key=True)


class BandBase(SQLModel):
    name: str
    genre: str


class BandCreate(BandBase):
    albums: list[AlbumBase] | None = None


class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)


class GenreURLChoices(Enum):
    ROCK = 'rock'
    JAZZ = 'jazz'
    HIPHOP = 'hip hop'
    POP = 'pop'
