from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from services.note_service import read_note, read_all_notes, create_note, update_note, delete_note
from core.database import get_db
from schemas.note import NoteRead, NoteCreate, NoteUpdate
from typing import List



router = APIRouter()

# READ NOTE:
@router.get("/api/v1/notes/{note_id}", response_model=NoteRead) #ENDPOINT + modello della risposta
#   nome        Ha come input notr_id e il db, che ottiene da get_db.       Usa NoteRead come responsemodel
def view_one_note(note_id: int, db: Session = Depends(get_db)) -> NoteRead:
    note = read_note(db, note_id) # usa classe services per leggere la nota
    return note #restituisce in base a response_model


@router.get("/api/v1/notes", response_model=List[NoteRead])
def view_all_notes(db: Session = Depends(get_db)) -> List[NoteRead]:
    note_list = read_all_notes(db)
    return note_list

# CREATE NOTE:
@router.post("/api/v1/notes", response_model=NoteRead) # metto NoteRead perche' cosi restituisco i dati
def create_new_note(note: NoteCreate, db: Session = Depends(get_db)) -> NoteRead:
    new_note = create_note(db, note)
    return new_note

# UPDATE NOTE:
@router.patch("/api/v1/notes/{note_id}", response_model=NoteRead)
def patch_note(note_id: int, data: NoteUpdate, db: Session = Depends(get_db)) -> NoteRead:
    updated = update_note(db, note_id, data)
    return updated

# DELETE NOTE:
@router.delete("/api/v1/notes/{note_id}", response_model=NoteRead)
def erase_note(note_id: int, db: Session = Depends(get_db)) -> NoteRead:
    note = delete_note(db, note_id)
    return note