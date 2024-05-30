from router.auth import auth_router
from router.tarjeta import tarjeta_router
from config.database import engine, Base
from fastapi import FastAPI
import socket
import redis
import os

app = FastAPI()
app.title = "Banco de los Alpes"
app.version = "0.0.1"

# app.add_middleware(ErrorHandler)
app.include_router(tarjeta_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

# Configuración de Redis
redis_host = os.environ.get("REDIS_HOST")
redis_port = os.environ.get("REDIS_PORT")

try:
    redis_client = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)
    redis_client.ping()  # Verificar la conexión
except redis.ConnectionError as e:
    print(f"Error al conectar a Redis: {e}")
    raise  # Detener la aplicación si no se puede conectar

@app.get('/')
def root():
    return {"id": socket.gethostname()}