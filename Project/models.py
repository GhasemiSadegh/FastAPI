from sqlmodel import SQLModel, Field
from database import engine


class BaseLibrary(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    author: str
    pub_year: int
    genre: str


SQLModel.metadata.create_all(engine)
