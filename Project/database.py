from sqlmodel import create_engine, Session, SQLModel

DB_URL = 'sqlite:///database.sqlite'
engine = create_engine(DB_URL)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
