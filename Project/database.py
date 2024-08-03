from sqlmodel import SQLModel, Session, create_engine, Field


DB_URL = 'sqlite:///database.sqlite'
engine = create_engine(DB_URL)


class Library(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    author: str
    pub_year: int
    genre: str


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


SQLModel.metadata.create_all(engine)
