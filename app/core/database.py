from sqlalchemy.orm import sessionmaker, declarative_base, Session, Generator
from datetime import datetime
import sqlalchemy as sa
from typing import Optional, Dict, List

# Initializazione DB
engine = sa.create_engine(
    'sqlite:///memory',
    echo=True, # echo per + dettagli
    SQLALCHEMY_Dconnect_args={"check_same_thread": False}
    ) 
# file locale: sqlite:///LibraryTools.db
# DB in RAM: sqlite:///:memory
Base = declarative_base() # usarto per dichiarare le tabelle


SessionLocal = sessionmaker(bind=engine) # CREA SESSIONE | bind: binda la sessione a questo db


# Dependency Injection | Chiamata al DB
def get_db() -> Generator:
    db = SessionLocal() # usa la sessione creata prima
    try:
        yield db
    finally:
        db.close()
