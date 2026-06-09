from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Tag
from typing import Dict
from exceptions import DuplicateResourceError, UnableToUpdateThisResource, ResourceNotFoundError

#-------LETTURA
def get_tag_by_id(db: Session, tag_id: int): 
    statement = select(Tag).where(Tag.id == tag_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_tag_by_label(db: Session, name: str): 
    statement = select(Tag).where(Tag.name == name) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_tags(db: Session):
    statement = select(Tag) # Uguale a SELECT * FROM Tags
    result = db.execute(statement)
    return result.scalars().all()

#-------CRUD
def save_tag(db: Session, tag: Tag):
    try:
        db.add(tag)
        db.commit() 
        db.refresh(tag) 
        return tag
    except:
        db.rollback()
        raise DuplicateResourceError("tag", tag.id)

def edit_tag (db: Session, tag: Tag, update_data: Dict): 
    try:
        for field, value in update_data.items():
            setattr(tag, field, value)# 
        db.commit()
        db.refresh(tag)
        return tag
    except:
        db.rollback()
        raise UnableToUpdateThisResource("repository", "edit_tag" , tag.id)

def remove_tag(db: Session, tag: Tag):
    try:
        db.delete(tag)
        db.commit()
        return tag
    except:
        db.rollback()
        raise ResourceNotFoundError("tag", tag.id)