import datetime

from sqlalchemy import Column, Float, Integer, String, DateTime
from config.database import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    cedula = Column(Integer, primary_key=True)
    nombre = Column(String)
    telefono = Column(String)
    email = Column(String)
    pais = Column(String)
    ciudad = Column(String)
    fechaRegistro = Column(DateTime, default=datetime.datetime.utcnow)

