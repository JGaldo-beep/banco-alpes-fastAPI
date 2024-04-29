from models.tarjeta import Tarjeta as TarjetaModel
from schemas.tarjeta import Tarjeta

class TarjetaService():

    def __init__(self, db) -> None:
        self.db = db
        
    def get_tarjetas(self):
        result = self.db.query(TarjetaModel).all()
        return result
    
    def get_tarjeta(self, id: int):
        result = self.db.query(TarjetaModel).filter(TarjetaModel.id == id).first()
        return result
    
    def get_tarjeta_by_category(self, category: str):
        result = self.db.query(TarjetaModel).filter(TarjetaModel.category == category).all()
        return result
    
    def create_tarjeta(self, tarjeta: Tarjeta):
        new_tarjeta = TarjetaModel(**tarjeta.model_dump())
        self.db.add(new_tarjeta)
        self.db.commit()
        return 
    
    def update_tarjeta(self, id: int, data: Tarjeta):
        tarjeta = self.db.query(TarjetaModel).filter(TarjetaModel.id == id).first()
        tarjeta.name_card = data.name_card
        tarjeta.card_type = data.card_type
        tarjeta.main_benefits = data.main_benefits
        tarjeta.annual_percentage_rate = data.annual_percentage_rate
        tarjeta.annual_fee = data.annual_fee
        tarjeta.minimum_requirements = data.minimum_requirements
        tarjeta.payments_options = data.payments_options
        tarjeta.credit_limit = data.credit_limit
        tarjeta.apply_online = data.apply_online
        self.db.commit()
        return
    
    def delete_tarjeta(self, id: int):
        self.db.query(TarjetaModel).filter(TarjetaModel.id == id).delete()
        self.db.commit()
        return