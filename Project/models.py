from sqlmodel import SQLModel, Field


class BaseLibrary(SQLModel):
    title: str
    author: str
    pub_year: int
    genre: str


class Library(BaseLibrary, table=True):
    id: int = Field(None, primary_key=True)