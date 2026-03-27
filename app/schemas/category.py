from pydantic import BaseModel, ConfigDict
from typing import Optional

# Definizione di un basemodel da passare in argomento alle altre classi
class CategoryBase(BaseModel):
    CatName: str
    Description: Optional[str] = None

# Se vuoi fare ulteriori verifiche qui, togli pass, CategoryBase e procedi. 
# altrimenti basta passare CategoryBase
class CategoryCreate(CategoryBase):
    pass

# Qui prende 1 o 2 parametri, se ci sono ok altrimenti nulla. Sono opzionali
class CategoryUpdate(BaseModel):
    CatName: Optional[str] = None
    Description: Optional[str] = None


class CategoryRead(CategoryBase):
    CatID: int

    # per trasformare oggetti DB in response JSON
    # Deve stare dentro lo schema che usi per le response:
    model_config = ConfigDict(from_attributes=True)

