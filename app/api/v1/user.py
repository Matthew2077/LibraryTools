from fastapi import Depends, FastAPI
from main import app
from sqlalchemy.orm import Session
from services.user_service import read_user, read_all_users
from core.database import get_db
from schemas.user import UserRead
from typing import List

# root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# READ USER:
@app.get("/api/v1/users/{user_id}", response_model=UserRead) 
def view_one_user(user_id: int, db: Session = Depends(get_db)) -> UserRead:
    user = read_user(db, user_id) 
    return {user}

@app.get("/api/v1/users", response_model=List[UserRead])
def view_all_users(db: Session = Depends(get_db)) -> List[UserRead]:
    user_list = read_all_users(db)
    return user_list