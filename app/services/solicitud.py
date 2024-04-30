from models.solicitud import Solicitud as SolicitudModel
from schemas.solicitud import Solicitud

from fastapi import APIRouter, Depends, Path, Query

class SolicitudService():
    
    def __init__(self, db) -> None:
        self.db = db
        
    def get_solicitudes(self):
        result = self.db.query(SolicitudModel).all()
        return result
    
    def get_solicitud(self, id: int):
        result = self.db.query(SolicitudModel).filter(SolicitudModel.id == id).first()
        return result
    def get_solicitud_by_solicitante(self, solicitante: str):
        result = self.db.query(SolicitudModel).filter(SolicitudModel.solicitante == solicitante).all()
        return result
    
    def get_solicitud_since(self, fechaYHora: str):
        result = self.db.query(SolicitudModel).filter(SolicitudModel.fechaYHora >= fechaYHora).all()
        return result
    
    def create_solicitud(self, solicitud: Solicitud):
        new_solicitud = SolicitudModel(**solicitud.model_dump())
        self.db.add(new_solicitud)
        self.db.commit()
        return 
    
    def update_solicitud(self, id: int, data: Solicitud):
        solicitud = self.db.query(SolicitudModel).filter(SolicitudModel.id == id).first()
        solicitud.solicitante = data.solicitante
        solicitud.fechaYHora = data.fechaYHora
        solicitud.profesion = data.profesion
        solicitud.ingresos = data.ingresos
        solicitud.deudas = data.deudas
        solicitud.empresaDeTrabajo = data.empresaDeTrabajo
        solicitud.tipoDeSoliticante = data.tipoDeSoliticante
        solicitud.tiempoDeSolitud = data.tiempoDeSolitud
        self.db.commit()
        return
    
    def update_solicitud_by_solicitante(self, solicitante: str, data: Solicitud):
        solicitud = self.db.query(SolicitudModel).filter(SolicitudModel.solicitante == solicitante).first()
        solicitud.solicitante = data.solicitante
        solicitud.fechaYHora = data.fechaYHora
        solicitud.profesion = data.profesion
        solicitud.ingresos = data.ingresos
        solicitud.deudas = data.deudas
        solicitud.empresaDeTrabajo = data.empresaDeTrabajo
        solicitud.tipoDeSoliticante = data.tipoDeSoliticante
        solicitud.tiempoDeSolitud = data.tiempoDeSolitud
        self.db.commit()
        return
    
    def delete_solicitud_by_solicitante(self, solicitante: str):
        self.db.query(SolicitudModel).filter(SolicitudModel.solicitante == solicitante).delete()
        self.db.commit()
        return
    
    def delete_solicitud(self, id: int):
        self.db.query(SolicitudModel).filter(SolicitudModel.id == id).delete()
        self.db.commit()
        return