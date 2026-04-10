from sqlalchemy.orm import Session
from repositories.user_repository import get_user_by_id, save_user, remove_user
from core.models import User

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

    return save_user

def update_user():

    return

def delete_user(db: Session, user_id: int):
    user = read_user(db, user_id)

    remove_user(db, user)

    return user