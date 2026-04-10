from typing import List
from sqlalchemy.orm import Session
from repositories.note_repository import save_note, get_note_by_id, remove_note
from repositories.tag_repository import get_tag_by_label, create_repo_tag
from repositories.category_repository import get_category_by_id
from core.models import Note, NoteState, Tag
from datetime import datetime

def read_note(db: Session, note_id: int):
    note = get_note_by_id(db, note_id)

    if not note:
        raise ValueError("Note not found")
    
    return note

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


def update_note():


    return

def delete_note(db: Session, note_id: int):
    note = read_note(db, note_id)

    remove_note(db, note)

    return note

def soft_delete_note(db: Session, note_id: int): # Esperimento 
    # Cambia lo stato della nota in ELIMINATO per renderlo non visibile.
    return