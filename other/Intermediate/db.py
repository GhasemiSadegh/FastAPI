from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = 'sqlite:///db.sqlite'
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:  # with closes the session closes properly
        yield session  # yields the session for use in operations
