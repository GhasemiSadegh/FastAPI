from sqlmodel import SQLModel, Field
from database import engine


class BaseLibrary(SQLModel):
    title: str
    author: str
    pub_year: int
    genre: str


class Library(BaseLibrary, table=True):
    id: int = Field(primary_key=True)


SQLModel.metadata.create_all(engine)