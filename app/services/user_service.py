from sqlalchemy.orm import Session
from repositories.user_repository import get_user_by_id, save_user, remove_user, edit_user
from core.models import User
from schemas.user import UserUpdate

def read_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    
    if not user:
        raise ValueError("user not found")
    return user

def create_user(db: Session, user_name: str, user_email: str | None = None, user_pswd: str | None = None):

    if user_name is None:
        raise ValueError("Username invalid")
    
    new_user = User(
        UserName = user_name,
        Email = user_email,
        Password = user_pswd
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