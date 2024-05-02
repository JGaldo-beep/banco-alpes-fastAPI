import datetime

from sqlalchemy.orm import Session
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

    @staticmethod
    def insertar_usuarios(session, lista_usuarios):
        try:
            for usuario_data in lista_usuarios:
                usuario = Usuario(
                    cedula=usuario_data['cedula'],
                    nombre=usuario_data['nombre'],
                    telefono=usuario_data['telefono'],
                    email=usuario_data['email'],
                    pais=usuario_data['pais'],
                    ciudad=usuario_data['ciudad'],
                    fechaRegistro=usuario_data.get('fechaRegistro', datetime.datetime.utcnow())
                )
                session.add(usuario)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

