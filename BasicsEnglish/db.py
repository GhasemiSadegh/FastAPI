from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = 'sqlite:///db.sqlite'
engine = create_engine(DATABASE_URL, echo=True)
