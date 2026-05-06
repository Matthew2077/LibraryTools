from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.tag_service import read_tag, read_all_tags, create_tag, update_tag, delete_tag
from core.database import get_db
from schemas.tag import TagRead, TagCreate, TagUpdate
from typing import List

router = APIRouter()

# READ TAG:
@router.get("/api/v1/tags/{tag_id}", response_model=TagRead) 
def view_one_tag(tag_id: int, db: Session = Depends(get_db)) -> TagRead:
    tag = read_tag(db, tag_id) 
    return {tag}


@router.get("/api/v1/tags", response_model=List[TagRead])
def view_all_tags(db: Session = Depends(get_db)) -> List[TagRead]:
    tag_list = read_all_tags(db)
    return tag_list

# CREATE TAG:
@router.post("/api/v1/tags", response_model=TagRead) 
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)) -> TagRead:
    new_tag = create_tag(db, tag)
    return new_tag

# UPDATE TAG:
@router.patch("/api/v1/tag/{tag_id}", response_model=TagRead)
def patch_tag(tag_id: int, data: TagUpdate, db: Session = Depends(get_db)) -> TagRead:
    updated = update_tag(db, tag_id, data)
    return updated

# DELETE TAG:
@router.delete("/api/v1/tag/{tag_id}", response_model=TagRead)
def erase_tag(tag_id: int, db: Session = Depends(get_db)) -> TagRead:
    tag = delete_tag(db, tag_id)
    return tag