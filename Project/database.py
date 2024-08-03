from sqlmodel import create_engine, Session

DB_URL = 'sqlite:///database.sqlite'
engine = create_engine(DB_URL)


def get_session():
    return Session(engine)
