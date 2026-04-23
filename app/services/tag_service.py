from sqlalchemy.orm import Session
from repositories.tag_repository import get_tag_by_id, save_tag, remove_tag, edit_tag, get_all_tags
from core.models import Tag
from schemas.tag import TagUpdate

def read_tag(db: Session, tag_id: int):
    
    tag = get_tag_by_id(db, tag_id)
    
    if not tag:
        raise ValueError("tag not found")
    return tag

def read_all_tags(db: Session):
    tag_list = get_all_tags(db)
    return tag_list


def create_tag(db: Session, label: str):

    if label is None:
        raise ValueError("Label invalid")
    
    normalized = label.strip().lower()

    new_tag = Tag(
        Label = normalized
    )

    saved_tag = save_tag(db, new_tag)
    return saved_tag

def update_tag(db: Session, tag_id: int, data: TagUpdate):
    if data is None:
        raise ValueError("No data uploaded")
    
    tag = read_tag(db, tag_id)
    update_data = data.model_dump(exclude_unset=True)
    
    if not update_data:
        raise ValueError("No fields to update")

    updated_tag = edit_tag(db, tag, update_data)

    return updated_tag

def delete_tag(db: Session, tag_id: int):
    tag = read_tag(db, tag_id)

    remove_tag(db, tag)

    return tag