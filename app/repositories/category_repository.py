from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import Category
from typing import Dict
from exceptions import DuplicateResourceError, UnableToUpdateThisResource, ResourceNotFoundError

#-------LETTURA
def get_category_by_id(db: Session, category_id: int): 
    statement = select(Category).where(Category.id == category_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_categories(db: Session):
    statement = select(Category) # Uguale a SELECT * FROM Categories
    result = db.execute(statement)
    return result.scalars().all()

def get_category_by_name(db: Session, category_name: str):
    statement = select(Category).where(Category.name == category_name)
    result = db.execute(statement)
    return result.scalar_one_or_none()

#-------CRUD
def save_category(db: Session, category: Category): 
    try:
        db.add(category)
        db.commit() 
        db.refresh(category)
        return category
    except:
        db.rollback()
        raise DuplicateResourceError("category", category.id)

def edit_category(db: Session, category: Category, update_data: Dict): # Session + Oggetto esistente + dati da aggiornare
    try:
        for field, value in update_data.items():
            setattr(category, field, value) 
        db.commit()
        db.refresh(category)
        return category
    except:
        db.rollback()
        raise UnableToUpdateThisResource("category", category.id)



def remove_category(db: Session, category: Category):
    try:
        db.delete(category)
        db.commit()
        return category
    except:
        db.rollback()
        raise ResourceNotFoundError("category", category.id)