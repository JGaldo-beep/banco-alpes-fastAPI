from sqlalchemy import Column, Float, Integer, String, Date
from config.database import Base

class Solicitud(Base):

    __tablename__= "solicitudes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha = Column(Date)
    ingresos = Column(Integer)
    tipoSolicitud = Column(String)
    tiempoSolicitud = Column(Integer)
