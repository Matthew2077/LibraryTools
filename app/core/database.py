from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base
from datetime import datetime
import sqlalchemy as sa
from typing import Optional, Dict, List

# Initializazione DB
engine = sa.create_engine('sqlite///memory:', echo=True) # echo per + dettagli
Session = sessionmaker(bind=db) # binda la sessione a questo db
Base = declarative_base() # ?? what is that

