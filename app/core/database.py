import sqlalchemy as sa
from typing import Generator
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

# Initializazione DB
engine = sa.create_engine(
    'sqlite:///LibraryTools.db',
    echo=True, # echo per + dettagli
    connect_args={"check_same_thread": False}
    ) 
# file locale: sqlite:///LibraryTools.db
# DB in RAM: sqlite:///:memory:
# se usi /// crea il db dove lanci il comando, sistema poi

class Base(DeclarativeBase): # usarto per dichiarare le tabelle
    pass 

SessionLocal = sessionmaker(bind=engine) # FABBRICA DI SESSIONI | bind: binda la sessione a questo db



# Dependency Injection | Chiamata al DB
def get_db() -> Generator:
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
