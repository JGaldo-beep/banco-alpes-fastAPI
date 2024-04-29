from typing import Optional
from pydantic import BaseModel, Field

#hola

class Solicitud(BaseModel):
    id: Optional[int] = None
    solicitante: str = Field(min_length = 5, max_length = 50)
    fechaYHora: str
    profesion: str = Field(min_length = 5, max_length = 50)
    ingresos: float
    deudas: float
    empresaDeTrabajo: str = Field(min_length = 5, max_length = 50)
    tipoDeSoliticante: str = Field(min_length = 5, max_length = 50)
    tiempoDeSolitud: str = Field(min_length = 5, max_length = 50)
    
    def model_dump(self):
        return {
            "id": self.id,
            "solicitante": self.solicitante,
            "fechaYHora": self.fechaYHora,
            "profesion": self.profesion,
            "ingresos": self.ingresos,
            "deudas": self.deudas,
            "empresaDeTrabajo": self.empresaDeTrabajo,
            "tipoDeSoliticante": self.tipoDeSoliticante,
            "tiempoDeSolitud": self.tiempoDeSolitud
        }