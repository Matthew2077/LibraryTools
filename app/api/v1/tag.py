from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.tag_service import read_tag, read_all_tags, create_tag, update_tag, delete_tag
from core.database import get_db
from schemas.tag_schemas import TagRead, TagCreate, TagUpdate
from typing import List

router = APIRouter()

# READ TAG:
@router.get("/{tag_id}", response_model=TagRead) 
def view_one_tag(tag_id: int, db: Session = Depends(get_db)) -> TagRead:
    return read_tag(db, tag_id) 


@router.get("/", response_model=List[TagRead])
def view_all_tags(db: Session = Depends(get_db)) -> List[TagRead]:
    return read_all_tags(db)

# CREATE TAG:
@router.post("/", response_model=TagRead) 
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)) -> TagRead:
    return create_tag(db, tag)

# UPDATE TAG:
@router.patch("/{tag_id}", response_model=TagRead)
def patch_tag(tag_id: int, data: TagUpdate, db: Session = Depends(get_db)) -> TagRead:
    return update_tag(db, tag_id, data)

# DELETE TAG:
@router.delete("/{tag_id}", response_model=TagRead)
def erase_tag(tag_id: int, db: Session = Depends(get_db)) -> TagRead:
    return delete_tag(db, tag_id)