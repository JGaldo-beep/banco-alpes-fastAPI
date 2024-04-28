from typing import List
from fastapi import APIRouter, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import Session
from middlewares.jwt_bearer import JWTBeater
from models.usuario import Usuario as UsuarioModel

from services.usuario import UsuarioService
from services.tarjeta import TarjetaService
from schemas.usuario import Usuario
from schemas.tarjeta import Tarjeta

usuario_router = APIRouter()

@usuario_router.get('/usuarios', tags = ['usuarios'], response_model = List[Usuario], status_code=200, dependencies=[Depends(JWTBeater())])
def get_usuarios() -> List[Tarjeta]:
    db = Session()
    result = TarjetaService(db).get_usuarios()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@usuario_router.get('/usuarios/{cedula}', tags = ['usuarios'], response_model = Usuario)
def get_usuario(cedula: int = Path(ge = 1, le = 2000)) -> Usuario:
    db = Session()
    result = UsuarioService(db).get_usuario(cedula)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found!"})
        
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@usuario_router.get('/usuarios/', tags = ['usuarios'], response_model = List[Usuario], status_code=200)
def get_usuarios_by_name(nombre: str = Query(min_length = 5, max_length = 15)):
    db = Session()
    result = UsuarioService(db).get_usuario_by_name(nombre)
    if not result:
        return JSONResponse(status_code=404, content = { "message": "Not found!" })
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@usuario_router.post('/usuarios', tags = ['usuarios'], response_model = dict, status_code=201)
def create_usuario(usuario: Usuario) -> dict:
        
        # Register a new usuario
        db = Session()
        UsuarioService(db).create_usuario(usuario)
        return JSONResponse(content = { "message": "usuario created!" }, status_code=201)

@usuario_router.put('/usuarios/{cedula}', tags = ['usuarios'], response_model = dict)
def update_usuario(cedula: int, usuario: Usuario) -> dict:
    db = Session()
    result = UsuarioService(db).get_usuario(cedula)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    UsuarioService(db).update_usuario(cedula, usuario)
    return JSONResponse(status_code=200, content={ "message": "Usuario updated!" })

@usuario_router.delete('/usuarios/{cedula}', tags = ['usuarios'], response_model = dict)
def delete_usuario(cedula: int) -> dict:
    db = Session()
    result: UsuarioModel = UsuarioService(db).get_usuario(cedula)
    if not result:
        JSONResponse(status_code=404, content={"message": "Not found!"})
    UsuarioService(db).delete_usuario(cedula)
    return JSONResponse(status_code=200, content={"message": "Usuario deleted!"})

@usuario_router.get('/usuarios/email/{email}', tags = ['usuarios'], response_model = Usuario)
def get_usuario_by_email(email: str = Path(min_length = 6, max_length = 50)) -> Usuario:
    db = Session()
    result = UsuarioService(db).get_usuario_by_email(email)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found!"})
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

