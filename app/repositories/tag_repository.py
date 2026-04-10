from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import Tag
from typing import Dict

#-------LETTURA
def get_tag_by_id(db: Session, tag_id: int): 
    statement = select(Tag).where(Tag.TagID == tag_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_tag_by_label(db: Session, tag_label: str): 
    statement = select(Tag).where(Tag.Label == tag_label) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_tags(db: Session):
    statement = select(Tag) # Uguale a SELECT * FROM Tags
    result = db.execute(statement)
    return result.scalars().all()

#-------CRUD
def save_tag(db: Session, tag: Tag): #Session + Oggetto SQLalchemy 
    db.add(tag) # aggiunge alla sessione
    db.commit() 
    db.refresh(tag) 
    return tag

def edit_tag (db: Session, tag: Tag, update_data: Dict): # Session + Oggetto esistente + dati da aggiornare
    for field, value in update_data.items():
        setattr(tag, field, value)# 
    db.commit()
    db.refresh(tag)
    return tag

def remove_tag(db: Session, tag: Tag):
    db.delete(tag)
    db.commit()
    db.refresh(tag)
    return tag