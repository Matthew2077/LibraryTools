from typing import List
from sqlalchemy.orm import Session
from repositories.note_repository import save_note, get_note_by_id, remove_note, edit_note, get_all_notes
from repositories.tag_repository import get_tag_by_label, create_repo_tag, get_tag_by_id
from repositories.category_repository import get_category_by_id
from core.models import Note, NoteState, Tag
from schemas.note import NoteUpdate
from datetime import datetime

def read_note(db: Session, note_id: int):
    note = get_note_by_id(db, note_id)

    if not note:
        raise ValueError("Note not found")
    
    return note

def read_all_notes(db: Session):
    note_list = get_all_notes(db)
    return note_list

def create_note(db: Session, title: str, body: str, category_id: int, Tags: List[str]):
    note_slug = title  # Da normalizzare in futuro
    author_id = 2155 # placeholder per v1 DEVE ESISTERE btw

    # verifica TAGS
    tag_list: List[Tag] = []
    for tag in Tags:
        verify_tag = get_tag_by_label(db, tag)
        if verify_tag is None:
            new_tag = Tag(Label = tag)
            # crealo nel Db
            create_repo_tag(db, new_tag)
            ## lo aggiungo alla lista
            tag_list.append(new_tag)
        else:
            tag_list.append(verify_tag)

    # verifica Category
    verify_category = get_category_by_id(db, category_id)
    if verify_category is None:
        raise ValueError("Category specified not found")

    note = Note(
        NoteSlug = note_slug, 
        Title = title,
        Body = body,
        State = NoteState.BOZZA, # Parte da Bozza

        ## Date Gestite
        DateCreation = datetime.now(),
        DateLastEdit = datetime.now(),

        ## FKs:
        CategoryID = category_id,
        AuthorID = author_id,
        tags = tag_list
    )

    # Crea Nota
    result = save_note(db, note)

    return result


def update_note(db: Session, note_id: int, data: NoteUpdate):
    if data is None:
        raise ValueError("No data uploaded")

    note = read_note(db, note_id)
    
    update_data = data.model_dump(exclude_unset=True)
    tag_ids = update_data.pop("TagIDs", None)
    
    
    if tag_ids is not None:
        tag_list = []
        for tag_id in tag_ids:
              tag = get_tag_by_id(db, tag_id) # leggi tag
              
              if tag is None:
                  raise ValueError(f"Tag with ID {tag_id} not found")
              tag_list.append(tag)

        note.tags = tag_list

    # Applica tutti gli altri campi
    for field, value in update_data.items():
          setattr(note, field, value)

    db.commit()
    db.refresh(note)

    return note



def delete_note(db: Session, note_id: int):
    note = read_note(db, note_id)

    remove_note(db, note)

    return note

def soft_delete_note(db: Session, note_id: int): # Esperimento 
    # Cambia lo stato della nota in ELIMINATO per renderlo non visibile.
    return