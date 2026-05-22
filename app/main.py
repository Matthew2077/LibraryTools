from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.v1 import note, category, tag, user
from core import Base, engine
import logging

# Avvio app fastapi
app = FastAPI(
    title="LibraryTools API",
    version="1.0.0",
    description="API per gestione note, categorie e tag"
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

### ESPERIMENTI ERROR HANDLING // deleting 
# 400 — dati non validi
@app.exception_handler(ValueError)
def value_error_handler(request: Request, exc: ValueError):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

# 404 — risorsa non trovata
@app.exception_handler(404)
def not_found_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=404,
        content={"detail": "Resource not found"}
    )

# 500 — errore generico non gestito
@app.exception_handler(Exception)
def generic_error_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


