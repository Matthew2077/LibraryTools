from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import Category
from typing import Dict

#-------LETTURA
def get_category_by_id(db: Session, category_id: int): 
    statement = select(Category).where(Category.CatID == category_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_categories(db: Session):
    statement = select(Category) # Uguale a SELECT * FROM Categories
    result = db.execute(statement)
    return result.scalars().all()

def get_category_by_name(db: Session, category_name: str):
    statement = select(Category).where(Category.CatName == category_name)
    result = db.execute(statement)
    return result.scalar_one_or_none()

#-------CRUD
def create(db: Session, category: Category): #Session + Oggetto SQLalchemy 
    db.add(category) # aggiunge alla sessione
    db.commit() 
    db.refresh(category) 
    return category

def update(db: Session, category: Category, update_data: Dict): # Session + Oggetto esistente + dati da aggiornare
    for field, value in update_data.items():
        setattr(category, field, value)# 
    db.commit()
    db.refresh(category)
    return category

def delete(db: Session, category: Category):
    db.delete(category)
    db.commit()
    db.refresh(category)
    return category