from fastapi import Depends, FastAPI
from main import app
from sqlalchemy.orm import Session
from services.tag_service import read_tag, read_all_tags
from core.database import get_db
from schemas.tag import TagRead
from typing import List

# root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# READ TAG:
@app.get("/api/v1/tags/{tag_id}", response_model=TagRead) 
def view_one_tag(tag_id: int, db: Session = Depends(get_db)) -> TagRead:
    tag = read_tag(db, tag_id) 
    return {tag}


@app.get("/api/v1/tags", response_model=List[TagRead])
def view_all_notes(db: Session = Depends(get_db)) -> List[TagRead]:
    tag_list = read_all_tags(db)
    return tag_list