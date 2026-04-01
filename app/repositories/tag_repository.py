from sqlalchemy import select
from sqlalchemy.orm import Session
from core.models import Tag

#-------LETTURA
def get_tag_by_id(db: Session, tag_id: int): 
    statement = select(Tag).where(Tag.TagID == tag_id) # questa e' difatti la quary
    result = db.execute(statement) # eseguo il codice
    return result.scalar_one_or_none()

def get_all_tags(db: Session):
    statement = select(Tag) # Uguale a SELECT * FROM Tags
    result = db.execute(statement)
    return result.scalars().all()