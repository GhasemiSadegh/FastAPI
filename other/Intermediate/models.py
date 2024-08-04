from enum import Enum
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from datetime import date


class AlbumBase(SQLModel):
    title: str
    release_date: date
    band_id: int | None = Field(foreign_key="band.id")


class Album(AlbumBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band: "Band" = Relationship(back_populates="albums")


class BandBase(SQLModel):
    name: str
    genre: str


class BandCreate(BandBase):
    albums: list[AlbumBase] | None = None


class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")


class GenreURLChoices(Enum):
    ROCK = 'rock'
    JAZZ = 'jazz'
    HIPHOP = 'hip hop'
    POP = 'pop'
