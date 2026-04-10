from sqlalchemy.orm import Session
from repositories.tag_repository import get_tag_by_id, save_tag, remove_tag
from core.models import Tag

def read_tag(db: Session, tag_id: int):
    
    tag = get_tag_by_id(db, tag_id)
    
    if not tag:
        raise ValueError("tag not found")
    return tag

def create_tag(db: Session, label: str):

    if label is None:
        raise ValueError("Label invalid")
    
    normalized = label.strip().lower()

    new_tag = Tag(
        Label = normalized
    )

    saved_tag = save_tag(db, new_tag)
    return saved_tag

def update_tag():

    return

def delete_tag(db: Session, tag_id: int):
    tag = read_tag(db, tag_id)

    remove_tag(db, tag)

    return tag