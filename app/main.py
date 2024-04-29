from middlewares.error_handler import ErrorHandler
from router.auth import auth_router
from router.tarjeta import tarjeta_router
from config.database import engine, Base
from fastapi import FastAPI
import socket

app = FastAPI()
app.title = 'Banco de los Alpes'
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(tarjeta_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {"id": socket.gethostname()}