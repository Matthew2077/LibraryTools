from typing import List
from sqlalchemy.orm import Session
from repositories.note_repository import save_note, get_note_by_id, remove_note, edit_note, get_all_notes
from repositories.tag_repository import get_tag_by_label, save_tag, get_tag_by_id
from repositories.category_repository import get_category_by_id
from core.models import Note, NoteState, Tag
from schemas.note_schemas import NoteUpdate, NoteCreate
from datetime import datetime

def generate_slug(title: str) -> str:
    return title.lower().strip().replace(" ", "-")

def read_note(db: Session, note_id: int):
    note = get_note_by_id(db, note_id)

    if not note:
        raise ValueError(f"Note {note_id} not found")
    
    return note

def read_all_notes(db: Session):
    note_list = get_all_notes(db)
    return note_list

def create_note(db: Session, note_data: NoteCreate):
    author_id = 1 # deve venire da notecreate
    category_id = note_data.category_id
    slug = generate_slug(note_data.title)

    # verifica TAGS
    tag_list: List[Tag] = []
    for tag_id in note_data.tag_ids:
        verify_tag = get_tag_by_id(db, tag_id)
        if verify_tag is None:
            raise ValueError(f"Tag {tag_id} not found")
        tag_list.append(verify_tag)

    # verifica Category
    verify_category = get_category_by_id(db, category_id)
    if verify_category is None:
        raise ValueError(f"Category {category_id} not found")

    note = Note(
        slug = slug,
        title = note_data.title,
        content = note_data.content,
        state = NoteState.BOZZA, # Parte da Bozza

        ## Date Gestite
        creation_date = datetime.now(),
        update_date = datetime.now(),
        publish_date = datetime.now(),

        ## FKs:
        category_id = category_id,
        author_id = author_id,
        tags = tag_list
    )

    # Crea Nota
    result = save_note(db, note)

    return result


def update_note(db: Session, note_id: int, data: NoteUpdate):
    note = read_note(db, note_id)
    
    update_data = data.model_dump(exclude_unset=True)
    tag_ids = update_data.pop("tags", None)
    
    
    if tag_ids is not None:
        tag_list = []
        for tag_id in tag_ids:
              tag = get_tag_by_id(db, tag_id) # leggi tag
              
              if tag is None:
                  raise ValueError(f"Tag with ID {tag_id} not found")
              tag_list.append(tag)

        note.tags = tag_list
    else:
        raise ValueError("No tag IDs")

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