from pydantic import BaseModel, ConfigDict
from typing import Optional
from schemas.tag import TagRead
from datetime import datetime

class NoteBase(BaseModel):
    title: str
    content: str
    category_id: int
    model_config = ConfigDict(from_attributes=True)
    

class NoteCreate(NoteBase):
    tag_ids: list[int] 
#in fase di creazione ricevo IDs e non oggetti Tag

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category_id: Optional[int] = None
    tags: Optional[list[TagRead]] = None
    model_config = ConfigDict(from_attributes=True)

class NoteRead(NoteBase):
    id: int
    title: str
    content: str
    category_id: int
    author_id: int
    creation_date: datetime
    update_date: datetime
    publish_date: datetime
    tags: list[TagRead]
    