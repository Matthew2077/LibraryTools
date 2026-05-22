from sqlalchemy.orm import Session
from repositories.user_repository import get_user_by_id, save_user, remove_user, edit_user, get_all_users
from core.models import User
from schemas.user_schemas import UserUpdate, UserCreate

def read_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    
    if not user:
        raise ValueError(f"user {user_id} not found")
    return user

def read_all_users(db: Session):
    user_list = get_all_users(db)
    return user_list

def create_user(db: Session, userdata: UserCreate):
    if userdata.name is None:
        raise ValueError(f"Username {userdata.name} invalid")

    new_user = User(
        name = userdata.name,
        email = userdata.email
    )
    saved_user = save_user(db, new_user)
    return saved_user

def update_user(db: Session, user_id: int, data: UserUpdate):
    if data is None:
        raise ValueError("No data uploaded")
    
    user = read_user(db, user_id)
    update_data = data.model_dump(exclude_unset=True)
    
    if not update_data:
        raise ValueError("No fields to update")

    updated_user = edit_user(db, user, update_data)
    return updated_user

def delete_user(db: Session, user_id: int):
    user = read_user(db, user_id)
    remove_user(db, user)
    return user