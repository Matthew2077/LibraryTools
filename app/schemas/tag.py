from pydantic import BaseModel, ConfigDict
from typing import Optional

class TagBase(BaseModel):
    Label: str

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    Label: Optional[str] = None

class TagRead(TagBase):
    TagID: int
    model_config = ConfigDict(from_attributes=True)

    