from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import User
from typing import Dict

#-------LETTURA
def get_user_by_id(db: Session, user_id: int): 
    statement = select(User).where(User.UserID == user_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_users(db: Session):
    statement = select(User) # Uguale a SELECT * FROM Users
    result = db.execute(statement)
    return result.scalars().all()

#-------CRUD
def save_user(db: Session, user: User): #Session + Oggetto SQLalchemy 
    db.add(user) # aggiunge alla sessione
    db.commit() 
    db.refresh(user) 
    return user

def edit_user(db: Session, user: User, update_data: Dict): # Session + Oggetto esistente + dati da aggiornare
    for field, value in update_data.items():
        setattr(user, field, value)# 
    db.commit()
    db.refresh(user)
    return user

def remove_user(db: Session, user: User):
    db.delete(user)
    db.commit()
    return user