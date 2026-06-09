from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import User
from typing import Dict
from exceptions import DuplicateResourceError, UnableToUpdateThisResource, ResourceNotFoundError

#-------LETTURA
def get_user_by_id(db: Session, user_id: int): 
    statement = select(User).where(User.id == user_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_users(db: Session):
    statement = select(User) # Uguale a SELECT * FROM Users
    result = db.execute(statement)
    return result.scalars().all()

#-------CRUD
def save_user(db: Session, user: User): #Session + Oggetto SQLalchemy 
    try:
        db.add(user)
        db.commit() 
        db.refresh(user) 
        return user
    except:
        db.rollback()
        raise DuplicateResourceError("user", user.id)

def edit_user(db: Session, user: User, update_data: Dict): 
    try:
        for field, value in update_data.items():
            setattr(user, field, value)# 
        db.commit()
        db.refresh(user)
        return user
    except:
        db.rollback()
        raise UnableToUpdateThisResource("repository", "edit_user" , user.id)

def remove_user(db: Session, user: User):
    try:
        db.delete(user)
        db.commit()
        return user
    except:
        db.rollback()
        raise ResourceNotFoundError("user", user.id)