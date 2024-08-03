from sqlmodel import SQLModel, Field
from database import engine
from datetime import date


class BaseLibrary(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(default=None, max_length=20, unique=True)
    author: str = Field(default=None, min_length=3)
    pub_year: date = Field(default=None, description='The year the book was published.')
    genre: str = Field(default=None, title='Genres')


SQLModel.metadata.create_all(engine)
