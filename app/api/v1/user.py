from fastapi import Depends, FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.user_service import read_user, read_all_users, create_user, update_user, delete_user
from core.database import get_db
from schemas.user import UserRead, UserCreate, UserUpdate
from typing import List


router = APIRouter()

# READ USER:
@router.get("/{user_id}", response_model=UserRead) 
def view_one_user(user_id: int, db: Session = Depends(get_db)) -> UserRead:
    user = read_user(db, user_id) 
    return user


@router.get("/users", response_model=List[UserRead])
def view_all_users(db: Session = Depends(get_db)) -> List[UserRead]:
    user_list = read_all_users(db)
    return user_list

# CREATE USERS:
@router.post("/users", response_model=UserRead) 
def create_new_user(user: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    new_user = create_user(db, user)
    return new_user


# UPDATE USER:
@router.patch("/user/{user_id}", response_model=UserRead)
def patch_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)) -> UserRead:
    updated = update_user(db, user_id, data)
    return updated


# DELETE USER:
@router.delete("/{user_id}", response_model=UserRead)
def erase_user(user_id: int, db: Session = Depends(get_db)) -> UserRead:
    user = delete_user(db, user_id)
    return user