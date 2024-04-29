from typing import List
from fastapi import APIRouter, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import Session
from middlewares.jwt_bearer import JWTBeater
from models.solicitud import Solicitud as SolicitudModel
from services.solicitud import SolicitudService
from schemas.solicitud import Solicitud

solicitud_router = APIRouter()

@solicitud_router.get('/solicitudes', tags=['solicitudes'], response_model=List[Solicitud], status_code=200, dependencies=[Depends(JWTBeater())])
def get_solicitudes() -> List[Solicitud]:
    db = Session()
    result = SolicitudService(db).get_solicitudes()
    return result

@solicitud_router.get('/solicitudes/{solicitud_id}', tags=['solicitudes'], response_model=Solicitud)
def get_solicitud(solicitud_id: int = Path(..., title="The ID of the solicitud to get")) -> Solicitud:
    db = Session()
    result = SolicitudService(db).get_solicitud(solicitud_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Solicitud not found"})
    return result

@solicitud_router.post('/solicitudes', tags=['solicitudes'], response_model=dict, status_code=201)
def create_solicitud(solicitud: Solicitud) -> dict:
    db = Session()
    SolicitudService(db).create_solicitud(solicitud)
    return JSONResponse(content={"message": "Solicitud created"}, status_code=201)

@solicitud_router.put('/solicitudes/{solicitud_id}', tags=['solicitudes'], response_model=dict)
def update_solicitud(solicitud_id: int, solicitud: Solicitud) -> dict:
    db = Session()
    result = SolicitudService(db).get_solicitud(solicitud_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Solicitud not found"})
    SolicitudService(db).update_solicitud(solicitud_id, solicitud)
    return JSONResponse(status_code=200, content={"message": "Solicitud updated"})

@solicitud_router.delete('/solicitudes/{solicitud_id}', tags=['solicitudes'], response_model=dict)
def delete_solicitud(solicitud_id: int) -> dict:
    db = Session()
    result = SolicitudService(db).get_solicitud(solicitud_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Solicitud not found"})
    SolicitudService(db).delete_solicitud(solicitud_id)
    return JSONResponse(status_code=200, content={"message": "Solicitud deleted"})
