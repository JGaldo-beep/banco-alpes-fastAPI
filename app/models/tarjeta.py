from sqlalchemy import Column, Float, Integer, String
from config.database import Base

class Tarjeta(Base):
    
    __tablename__ = "tarjetas"
    
    id = Column(Integer, primary_key=True)
    tipoDeTarjeta = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)