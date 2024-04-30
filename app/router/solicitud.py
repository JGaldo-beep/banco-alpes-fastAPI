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

# @solicitud_router.get('/solicitudes', tags = ['solicitudes'], response_model = List[Solicitud], status_code=200, dependencies=[Depends(JWTBeater())])
# def get_solicitudes() -> List[Solicitud]:
#     db = Session()
#     result = SolicitudService(db).get_solicitudes()
#     return JSONResponse(status_code=200, content = jsonable_encoder(result))

@solicitud_router.get('/solicitudes', tags = ['solicitudes'], response_model = List[Solicitud], status_code=200)
def get_solicitudes() -> List[Solicitud]:
    db = Session()
    result = SolicitudService(db).get_solicitudes()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@solicitud_router.get('/solicitudes/{id}', tags = ['solicitudes'], response_model = Solicitud)
def get_solicitud(id: int = Path(ge = 1, le = 2000)) -> Solicitud:
    db = Session()
    result = SolicitudService(db).get_solicitud(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found!"})
        
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@solicitud_router.get('/solicitudes/', tags = ['solicitudes'], response_model = List[Solicitud], status_code=200)
def get_solicitudes_by_solicitante(solicitante: str = Query(min_length = 5, max_length = 50)):
    db = Session()
    result = SolicitudService(db).get_solicitud_by_solicitante(solicitante)
    if not result:
        return JSONResponse(status_code=404, content = { "message": "Not found!" })
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@solicitud_router.get('/solicitudes/', tags = ['solicitudes'], response_model = List[Solicitud], status_code=200)
def get_solicitudes_since(fechaYHora: str = Query(min_length = 5, max_length = 50)):
    db = Session()
    result = SolicitudService(db).get_solicitud_since(fechaYHora)
    if not result:
        return JSONResponse(status_code=404, content = { "message": "Not found!" })
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@solicitud_router.post('/solicitudes', tags = ['solicitudes'], response_model = dict, status_code=201)

def create_solicitud(solicitud: Solicitud) -> dict:
        
        # Register a new solicitud
        db = Session()
        SolicitudService(db).create_solicitud(solicitud)
        return JSONResponse(content = { "message": "solicitud created!" }, status_code=201)


@solicitud_router.put('/solicitudes/{solicitud_id}', tags = ['solicitudes'], response_model = dict)

def update_solicitud(id: int, solicitud: Solicitud) -> dict:
    db = Session()
    result = SolicitudService(db).get_solicitud(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    SolicitudService(db).update_solicitud(id, solicitud)
    return JSONResponse(status_code=200, content={ "message": "Solicitud updated!" })

def update_solicitud_by_solicitante(solicitante: str, solicitud: Solicitud) -> dict:
    db = Session()
    result = SolicitudService(db).get_solicitud_by_solicitante(solicitante)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    SolicitudService(db).update_solicitud_by_solicitante(solicitante, solicitud)
    return JSONResponse(status_code=200, content={ "message": "Solicitud updated!" })

def delete_solicitud_by_solicitante(solicitante: str) -> dict:
    db = Session()
    result: SolicitudModel = SolicitudService(db).get_solicitud_by_solicitante(solicitante)
    if not result:
        JSONResponse(status_code=404, content={"message": "Not found!"})
    SolicitudService(db).delete_solicitud_by_solicitante(solicitante)

@solicitud_router.delete('/solicitudes/{solicitud_id}', tags = ['solicitudes'], response_model = dict)
def delete_solicitud(id: int) -> dict:
    db = Session()
    result: SolicitudModel = SolicitudService(db).get_solicitud(id)
    if not result:
        JSONResponse(status_code=404, content={"message": "Not found!"})
    SolicitudService(db).delete_solicitud(id)





