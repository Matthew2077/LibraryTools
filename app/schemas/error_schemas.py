# schemas.py o exceptions.py
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str        # codice machine-readable, es. "note_not_found"
    detail: str       # messaggio human-readable


    # in futuro: 
    # timestamp, request_id, ecc.