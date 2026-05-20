from pydantic import BaseModel, ConfigDict
from typing import Optional

# Definizione di un basemodel da passare in argomento alle altre classi
class CategoryBase(BaseModel):
    name: str
    label: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    label: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class CategoryRead(CategoryBase):
    id: int
    name: str
    label: Optional[str] = None
    

