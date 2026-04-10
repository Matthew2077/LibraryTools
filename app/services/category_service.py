from sqlalchemy.orm import Session
from repositories.category_repository import get_category_by_id, save_category, remove_category
from core.models import Category

def read_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    
    if not category:
        raise ValueError("Category not found")
    return category

def create_category(db: Session, category: str, label: str | None = None):

    if category is None:
        raise ValueError("Category name invalid")
    
    new_category = Category(
        CatName = category,
        Description = label
    )

    saved_category = save_category(db, new_category)

    return saved_category

def update_category():

    return

def delete_category(db: Session, category_id: int):
    # devi cambiare categoria a tutte quelle categorie interessate

    category = read_category(db, category_id)

    remove_category(db, category)

    return category