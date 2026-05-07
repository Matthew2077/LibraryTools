from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    UserName: str
    Email: Optional[str] = None
    Password: Optional[str] = None
    
class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    UserName: Optional[str] = None
    Email: Optional[str] = None
    Password: Optional[str] = None

class UserRead(UserBase):
    UserID: int
    model_config = ConfigDict(from_attributes=True)
