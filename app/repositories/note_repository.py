from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import Note, NoteState

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