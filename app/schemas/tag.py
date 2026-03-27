from pydantic import BaseModel, ConfigDict
from typing import Optional

class TagBase(BaseModel):
    label: str

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    label: Optional[str] = None

class TagRead(TagBase):
    TagID: int
    model_config = ConfigDict(from_attributes=True)

    