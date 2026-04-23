from fastapi import Depends, FastAPI
from main import app
from sqlalchemy.orm import Session
from services.category_service import read_category, read_all_categories
from core.database import get_db
from schemas.category import CategoryRead
from typing import List

# root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# READ CATEGORY:
@app.get("/api/v1/categories/{category_id}", response_model=CategoryRead) 
def read_one_category(category_id: int, db: Session = Depends(get_db)) -> CategoryRead:
    category = read_category(db, category_id)
    return {category}


@app.get("/api/v1/categories", response_model=List[CategoryRead])
def view_all_categories(db: Session = Depends(get_db)) -> List[CategoryRead]:
    category_list = read_all_categories(db)
    return category_list
