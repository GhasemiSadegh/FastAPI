from sqlmodel import SQLModel, create_engine, Session


DB_URL = 'sqlite:///database.sqlite'
engine = create_engine(DB_URL)


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


SQLModel.metadata.create_all(engine)
