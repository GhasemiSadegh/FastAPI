from enum import Enum
from pydantic import BaseModel


class Band(BaseModel):
    id: int
    name: str
    genre: str


class GenreURLChoices(Enum):
    ROCK = 'rock'
    JAZZ = 'jazz'
    HIPHOP = 'hip hop'
    POP = 'pop'