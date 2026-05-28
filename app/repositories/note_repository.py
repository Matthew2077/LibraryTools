from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Note, NoteState, NoteTag
from typing import Dict
from exceptions import DuplicateResourceError, LibraryToolsError

#-------LETTURA
def get_note_by_id(db: Session, note_id: int):
    statement = select(Note).where(Note.id == note_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none() # scalar_one_or_none: ritorna il risultato come uno scalar o None se non ce' risultato

def get_all_notes(db: Session):
    statement = select(Note) # Uguale a SELECT * FROM Notes
    result = db.execute(statement)
    return result.scalars().all()

def get_note_by_slug(db: Session, note_slug: str):
    statement = select(Note).where(Note.slug == note_slug)
    result = db.execute(statement)
    return result.scalar_one_or_none() # e' unique quindi non ha senso mettere scalars().all()


def get_note_by_state(db: Session, note_state: NoteState):
    statement = select(Note).where(Note.state == note_state)
    result = db.execute(statement)
    return result.scalar_one_or_none()

def get_by_category_id(db: Session, cat_id: int): # restituisce tutte le note in quella categoria
    statement = select(Note).where(Note.id == cat_id)
    result = db.execute(statement)
    return result.scalars().all()

def get_by_tag_id(db: Session, tag_id: int):
    # Seleziona tutte le note, joina NoteTag, filtra per tag id richiesto
    statement = select(Note).join(NoteTag).where(NoteTag.tag_id == tag_id)
    result = db.execute(statement)
    return result.scalars().all()

#-------CRUD
def save_note(db: Session, note: Note): #Session + Oggetto SQLalchemy Note
    try:
        db.add(note)
        db.commit() 
        db.refresh(note)
        return note
    except IntegrityError:
        db.rollback()
        raise DuplicateResourceError("note", note.id)
    

def edit_note(db: Session, note: Note, update_data: Dict): 
    try: 
        for field, value in update_data.items():
            setattr(note, field, value)
        db.commit()
        db.refresh(note)
        return note
    except:
        db.rollback()
        raise LibraryToolsError("repository", "edit_note" , note.id)

def remove_note(db: Session, note: Note):
    db.delete(note)
    db.commit()
    return note