from typing import Optional
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    cedula: Optional[int] = None
    nombre: str = Field(min_length = 3, max_length = 50)
    telefono: str = Field(min_length = 7, max_length = 15)
    email: str = Field(min_length = 6, max_length = 50)
    pais: str = Field(min_length = 3, max_length = 50)
    ciudad: str = Field(min_length = 3, max_length = 50)
    class Config:
        orm_mode = True