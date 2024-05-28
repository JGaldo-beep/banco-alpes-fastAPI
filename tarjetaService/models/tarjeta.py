from sqlalchemy import Column, Float, Integer, String, Boolean
from config.database import Base

class Tarjeta(Base):
    
    __tablename__ = "tarjetas"
    
    id = Column(Integer, primary_key=True)
    name_card = Column(String)
    card_type = Column(String)
    main_benefits = Column(String)
    annual_percentage_rate = Column(Float)
    annual_fee = Column(Float)
    minimum_requirements = Column(String)
    payments_options = Column(String)
    credit_limit = Column(Float)
    apply_online = Column(Boolean)