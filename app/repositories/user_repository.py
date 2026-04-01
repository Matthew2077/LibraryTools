from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import User

#-------LETTURA
def get_user_by_id(db: Session, user_id: int): 
    statement = select(User).where(User.UserID == user_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_users(db: Session):
    statement = select(User) # Uguale a SELECT * FROM Users
    result = db.execute(statement)
    return result.scalars().all()

