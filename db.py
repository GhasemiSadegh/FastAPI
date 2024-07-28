from sqlmodel import Session, create_engine, SQLModel
DATABASE_URL = 'sqlite:///db.sqlite'
engine = create_engine(DATABASE_URL)
from fastapi import FastAPI




def init_db():
    SQLModel.metadata.create_all(engine)
