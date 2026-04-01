from sqlalchemy.orm import sessionmaker, declarative_base, Session
import sqlalchemy as sa
from typing import Generator


# Initializazione DB
engine = sa.create_engine(
    'sqlite:///:memory:',
    echo=True, # echo per + dettagli
    connect_args={"check_same_thread": False}
    ) 
# file locale: sqlite:///LibraryTools.db
# DB in RAM: sqlite:///:memory:
Base = declarative_base() # usarto per dichiarare le tabelle


SessionLocal = sessionmaker(bind=engine) # FABBRICA DI SESSIONI | bind: binda la sessione a questo db


# Dependency Injection | Chiamata al DB
def get_db() -> Generator:
    db = SessionLocal() # usa la sessione creata prima
    try:
        yield db
    finally:
        db.close()
