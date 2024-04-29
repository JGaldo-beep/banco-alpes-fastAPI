from sqlalchemy import Column, Float, Integer, String
from config.database import Base

class Solicitud(Base):
    
    __tablename__ = "solicitudes"
    
    id = Column(Integer, primary_key=True)
    solicitante = Column(String)
    fechaYHora = Column(String)
    profesion = Column(String)
    ingresos = Column(Float)
    deudas = Column(Float)
    empresaDeTrabajo = Column(String)
    tipoDeSoliticante = Column(String)
    tiempoDeSolitud = Column(String)
