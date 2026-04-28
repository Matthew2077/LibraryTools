from pydantic import BaseModel, ConfigDict
from typing import Optional

from schemas.tag import TagRead

class NoteBase(BaseModel):
    Title: str
    Body: str
    CategoryID: int
    TagIDs: list[int]

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    Title: Optional[str] = None
    Body: Optional[str] = None
    CategoryID: Optional[int] = None
    TagIDs: Optional[list[int]] = None

class NoteRead(NoteBase):
    NoteID: int
    tags: list[TagRead]
    model_config = ConfigDict(from_attributes=True)

