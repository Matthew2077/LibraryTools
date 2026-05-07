from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from api.v1 import note, category, tag, user
from core import Base, engine
#from core.models import User

# Avvio app fastapi
app = FastAPI(
    title="LibraryTools API",
    version="1.0.0",
    description="API per gestione note, categorie e tag"
)

# crea tutte le tabelle
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(note.router, prefix="/api/v1/notes", tags=["Notes"])
app.include_router(category.router, prefix="/api/v1/categories", tags=["Categories"])
app.include_router(tag.router, prefix="/api/v1/tags", tags=["Tags"])
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])


@app.get("/")
def root():
    return {"message": "LibraryTools API is running"}

