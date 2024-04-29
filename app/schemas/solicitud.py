from typing import Optional
from pyantic import BaseModel, Field

class SolicitudSchema(BaseModel):

    id: Optional[int] = None
    nombre: str
    fecha: str  
    ingresos: int
    tipoSolicitud: str
    tiempoSolicitud: int