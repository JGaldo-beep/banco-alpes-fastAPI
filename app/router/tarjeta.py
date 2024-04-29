from typing import List
from fastapi import APIRouter, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import Session
from middlewares.jwt_bearer import JWTBeater
from models.tarjeta import Tarjeta as TarjetaModel

from services.tarjeta import TarjetaService
from schemas.tarjeta import Tarjeta

tarjeta_router = APIRouter()

# @tarjeta_router.get('/tarjetas', tags = ['tarjetas'], response_model = List[Tarjeta], status_code=200, dependencies=[Depends(JWTBeater())])
# def get_tarjetas() -> List[Tarjeta]:
#     db = Session()
#     result = TarjetaService(db).get_tarjetas()
#     return JSONResponse(status_code=200, content = jsonable_encoder(result))

@tarjeta_router.get('/tarjetas', tags = ['tarjetas'], response_model = List[Tarjeta], status_code=200)
def get_tarjetas() -> List[Tarjeta]:
    db = Session()
    result = TarjetaService(db).get_tarjetas()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@tarjeta_router.get('/tarjetas/{id}', tags = ['tarjetas'], response_model = Tarjeta)
def get_tarjeta(id: int = Path(ge = 1, le = 2000)) -> Tarjeta:
    db = Session()
    result = TarjetaService(db).get_tarjeta(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found!"})
        
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@tarjeta_router.get('/tarjetas/', tags = ['tarjetas'], response_model = List[Tarjeta], status_code=200)
def get_tarjetas_by_category(category: str = Query(min_length = 5, max_length = 15)):
    db = Session()
    result = TarjetaService(db).get_tarjeta_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content = { "message": "Not found!" })
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@tarjeta_router.post('/tarjetas', tags = ['tarjetas'], response_model = dict, status_code=201)
def create_tarjeta(tarjeta: Tarjeta) -> dict:
    
    # Register a new tarjeta
    db = Session()
    TarjetaService(db).create_tarjeta(tarjeta)
    return JSONResponse(content = { "message": "tarjeta created!" }, status_code=201)

@tarjeta_router.put('/tarjetas/{tarjeta_id}', tags = ['tarjetas'], response_model = dict)
def update_tarjeta(id: int, tarjeta: Tarjeta) -> dict:
    db = Session()
    result = TarjetaService(db).get_tarjeta(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    TarjetaService(db).update_tarjeta(id, tarjeta)
    return JSONResponse(status_code=200, content={ "message": "Tarjeta updated!" })
        
@tarjeta_router.delete('/tarjetas/{tarjeta_id}', tags = ['tarjetas'], response_model = dict)
def delete_tarjeta(id: int) -> dict:
    db = Session()
    result: TarjetaModel = TarjetaService(db).get_tarjeta(id)
    if not result:
        JSONResponse(status_code=404, content={"message": "Not found!"})
    TarjetaService(db).delete_tarjeta(id)
    return JSONResponse(status_code=200, content={"message": "Tarjeta deleted Succesfully!"})