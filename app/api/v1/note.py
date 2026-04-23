from fastapi import Depends, FastAPI
from main import app
from sqlalchemy.orm import Session
from services.note_service import read_note, read_all_notes, create_note
from core.database import get_db
from schemas.note import NoteRead, NoteCreate
from typing import List


# root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# READ NOTE:
@app.get("/api/v1/notes/{note_id}", response_model=NoteRead) #ENDPOINT + modello della risposta
#   nome        Ha come input notr_id e il db, che ottiene da get_db.       Usa NoteRead come responsemodel
def view_one_note(note_id: int, db: Session = Depends(get_db)) -> NoteRead:
    note = read_note(db, note_id) # usa classe services per leggere la nota
    return note #restituisce in base a response_model


@app.get("/api/v1/notes", response_model=List[NoteRead])
def view_all_notes(db: Session = Depends(get_db)) -> List[NoteRead]:
    note_list = read_all_notes(db)
    return note_list

# TO FIX ---
@app.post("/api/v1/create_new", response_model=NoteRead) # metto NoteRead perche' cosi restituisco i dati
def create_new_note(title, body, category_id, tags: List[str], db: Session = Depends(get_db)) -> NoteRead:
    note = create_note(db, title, body, category_id, tags)
    return note