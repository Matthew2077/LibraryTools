from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import Category

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