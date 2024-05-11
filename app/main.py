#from middlewares.error_handler import ErrorHandler
from fastapi.responses import JSONResponse
from router.auth import auth_router
from router.tarjeta import tarjeta_router
from router.solicitud import solicitud_router
from config.database import engine, Base
from router.usuario import usuario_router
from fastapi import FastAPI


import socket

app = FastAPI()
app.title = 'Banco de los Alpes'
app.version = "0.0.1"

#app.add_middleware(ErrorHandler)
app.include_router(tarjeta_router)
app.include_router(auth_router)
app.include_router(solicitud_router)
app.include_router(usuario_router)

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {"id": socket.gethostname()}
