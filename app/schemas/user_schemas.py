from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
    
class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class UserRead(UserBase):
    id: int