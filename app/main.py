from fastapi import FastAPI
from api.v1 import note, category, tag, user
from core import Base, engine
import logging

# Avvio app fastapi
app = FastAPI(
    title="LibraryTools API",
    version="1.0.0",
    description="""A lightweight, API-first backend for managing and structuring knowledge through notes, categories, and tags.
Built with **FastAPI** and **SQLAlchemy 2.0**, designed for clarity and future growth.
    **View GitHub page:** github.com/Matthew2077/LibraryTools
"""
)

logger = logging.getLogger(__name__)

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
