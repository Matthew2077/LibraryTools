from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.category_service import read_category, read_all_categories, create_category, update_category, delete_category
from core.database import get_db
from schemas.category import CategoryRead, CategoryCreate, CategoryUpdate
from typing import List

router = APIRouter()

# READ CATEGORY:
@router.get("/api/v1/categories/{category_id}", response_model=CategoryRead) 
def read_one_category(category_id: int, db: Session = Depends(get_db)) -> CategoryRead:
    category = read_category(db, category_id)
    return category


@router.get("/api/v1/categories", response_model=List[CategoryRead])
def view_all_categories(db: Session = Depends(get_db)) -> List[CategoryRead]:
    category_list = read_all_categories(db)
    return category_list

# CREATE CATEGORY:
@router.post("/api/v1/categories", response_model=CategoryRead) 
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)) -> CategoryRead:
    new_category = create_category(db, category)
    return new_category

# UPDATE CATEGORY:
@router.patch("/api/v1/category/{category_id}", response_model=CategoryRead)
def patch_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)) -> CategoryRead:
    updated = update_category(db, category_id, data)
    return updated

# DELETE CATEGORY:
@router.delete("/api/v1/category/{category_id}", response_model=CategoryRead)
def erase_category(category_id: int, db: Session = Depends(get_db)) -> CategoryRead:
    category = delete_category(db, category_id)
    return category