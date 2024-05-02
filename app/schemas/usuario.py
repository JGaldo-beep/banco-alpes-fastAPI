import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, validator

class Usuario(BaseModel):
    cedula: Optional[int] = None
    nombre: str = Field(min_length = 3, max_length = 50)
    telefono: str = Field(min_length = 7, max_length = 15)
    email: str = Field(min_length = 6, max_length = 50)
    pais: str = Field(min_length = 3, max_length = 50)
    ciudad: str = Field(min_length = 3, max_length = 50)
    fechaRegistro: datetime.datetime

    
    class Config:
        orm_mode = True

    @validator('fechaRegistro', pre=True)
    def check_fecha(cls, v):
        if isinstance(v, datetime.datetime):
            return v
        try:
            return datetime.datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("fechaRegistro debe ser una fecha válida en formato YYYY-MM-DD")