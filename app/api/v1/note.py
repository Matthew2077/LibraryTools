from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from services.note_service import read_note, read_all_notes, create_note, update_note, delete_note
from core.database import get_db
from schemas.note_schemas import NoteRead, NoteCreate, NoteUpdate
from typing import List



router = APIRouter()

# READ NOTE:
@router.get("/{note_id}", response_model=NoteRead) #ENDPOINT + modello della risposta
#   nome        Ha come input notr_id e il db, che ottiene da get_db.       Usa NoteRead come responsemodel
def view_one_note(note_id: int, db: Session = Depends(get_db)) -> NoteRead:
    return read_note(db, note_id)


@router.get("/", response_model=List[NoteRead])
def view_all_notes(db: Session = Depends(get_db)) -> List[NoteRead]:
    return read_all_notes(db)

# CREATE NOTE:
@router.post("/", response_model=NoteRead) # metto NoteRead perche' cosi restituisco i dati
def create_new_note(note: NoteCreate, db: Session = Depends(get_db)) -> NoteRead:
    return create_note(db, note)

# UPDATE NOTE:
@router.patch("/{note_id}", response_model=NoteRead)
def patch_note(note_id: int, data: NoteUpdate, db: Session = Depends(get_db)) -> NoteRead:
    return update_note(db, note_id, data)

# DELETE NOTE:
@router.delete("/{note_id}", response_model=NoteRead)
def erase_note(note_id: int, db: Session = Depends(get_db)) -> NoteRead:
    return delete_note(db, note_id)