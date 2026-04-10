from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import Note, NoteState, NoteTag
from schemas.note import NoteCreate
from typing import Dict

#-------LETTURA
def get_note_by_id(db: Session, note_id: int):
    statement = select(Note).where(Note.NoteID == note_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none() # scalar_one_or_none: ritorna il risultato come uno scalar o None se non ce' risultato

def get_all_notes(db: Session):
    statement = select(Note) # Uguale a SELECT * FROM Notes
    result = db.execute(statement)
    return result.scalars().all()

def get_note_by_slug(db: Session, Note_slug: str):
    statement = select(Note).where(Note.NoteSlug == Note_slug)
    result = db.execute(statement)
    return result.scalar_one_or_none() # e' unique quindi non ha senso mettere scalars().all()


def get_note_by_state(db: Session, Note_state: NoteState):
    statement = select(Note).where(Note.State == Note_state)
    result = db.execute(statement)
    return result.scalar_one_or_none()

def get_by_category_id(db: Session, cat_id: int): # restituisce tutte le note in quella categoria
    statement = select(Note).where(Note.CategoryID == cat_id)
    result = db.execute(statement)
    return result.scalars().all()

def get_by_tag_id(db: Session, tag_id: int):
    # Seleziona tutte le note, joina NoteTag, filtra per tag id richiesto
    statement = select(Note).join(NoteTag).where(NoteTag.tag_id == tag_id)
    result = db.execute(statement)
    return result.scalars().all()

#-------CRUD
def save_note(db: Session, note: Note): #Session + Oggetto SQLalchemy Note
    db.add(note) # aggiunge alla sessione
    db.commit() #eseguo, lo scrivo nel db
    db.refresh(note) #ritorno allo stato iniziale per chiudere il flusso della funzione
    return note

def edit_note(db: Session, note: Note, update_data: Dict): # Session + Oggetto esistente + dati da aggiornare
    for field, value in update_data.items():
        setattr(note, field, value)# versione light di note.Title = ... note.Body = ... note.State = ...
    db.commit()
    db.refresh(note)
    return note

def remove_note(db: Session, note: Note):
    db.delete(note)
    db.commit()
    db.refresh(note)
    return note