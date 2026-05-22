from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.user_service import read_user, read_all_users, create_user, update_user, delete_user
from core.database import get_db
from schemas.user_schemas import UserRead, UserCreate, UserUpdate
from typing import List


router = APIRouter()

# READ USER:
@router.get("/{user_id}", response_model=UserRead) 
def view_one_user(user_id: int, db: Session = Depends(get_db)) -> UserRead:
    return read_user(db, user_id) 


@router.get("/", response_model=List[UserRead])
def view_all_users(db: Session = Depends(get_db)) -> List[UserRead]:
    return read_all_users(db)

# CREATE USERS:
@router.post("/", response_model=UserRead) 
def create_new_user(user: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    return create_user(db, user)


# UPDATE USER:
@router.patch("/{user_id}", response_model=UserRead)
def patch_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)) -> UserRead:
    return update_user(db, user_id, data)


# DELETE USER:
@router.delete("/{user_id}", response_model=UserRead)
def erase_user(user_id: int, db: Session = Depends(get_db)) -> UserRead:
    return delete_user(db, user_id)