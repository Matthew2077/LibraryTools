from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from core import Base
from .core.models import User

# Avvio app fastapi
app = FastAPI()


# PROVVISORIO... 

# def main() -> None:
#     Base.metadata.create_all(db)
#     user = User(username="Matthew", email="matthew@gmail.com")
# # START SESSIONE 
#     with Session() as session:
#         # QUI DEVI AGGIUNGERCI I VARI OGGETTI
#         session.add(user)
#         session.commit()
#         print(session.query(User).all())

