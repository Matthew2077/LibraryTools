from pydantic import BaseModel, ConfigDict
from typing import Optional

from schemas.tag import TagRead

class NoteBase(BaseModel):
    Title: str
    Body: str
    CategoryID: int
    

class NoteCreate(NoteBase):
    TagID: list[int]

class NoteUpdate(BaseModel):
    Title: Optional[str] = None
    Body: Optional[str] = None
    CategoryID: Optional[int] = None
    TagID: Optional[list[int]] = None

class NoteRead(NoteBase):
    NoteID: int
    #Tags: list[TagRead]
    model_config = ConfigDict(from_attributes=True)

