from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.category_service import read_category, read_all_categories, create_category, update_category, delete_category
from core.database import get_db
from schemas.category_schemas import CategoryRead, CategoryCreate, CategoryUpdate
from typing import List

router = APIRouter()

# READ 
@router.get("/{category_id}", response_model=CategoryRead) 
def read_one_category(category_id: int, db: Session = Depends(get_db)) -> CategoryRead:
    return read_category(db, category_id)

# /api/v1/categories/
@router.get("/", response_model=List[CategoryRead])
def view_all_categories(db: Session = Depends(get_db)) -> List[CategoryRead]:
    return read_all_categories(db)

# CREATE : /api/v1/category
@router.post("/", response_model=CategoryRead) 
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)) -> CategoryRead:
    return create_category(db, category)

# UPDATE CATEGORY:
@router.patch("/{category_id}", response_model=CategoryRead)
def patch_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)) -> CategoryRead:
    return update_category(db, category_id, data)

# DELETE CATEGORY:
@router.delete("/{category_id}", response_model=CategoryRead)
def erase_category(category_id: int, db: Session = Depends(get_db)) -> CategoryRead:
    return delete_category(db, category_id)