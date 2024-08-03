from sqlmodel import SQLModel, Session, create_engine, Field
from typing import Optional

DB_URL = 'sqlite:///database.sqlite'
engine = create_engine(DB_URL)


class BaseLibrary(SQLModel):
    title: str
    author: str
    pub_year: int
    genre: str


class Library(BaseLibrary, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


SQLModel.metadata.create_all(engine)
