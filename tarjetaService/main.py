from router.auth import auth_router
from router.tarjeta import tarjeta_router
from config.database import engine, Base
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import socket
import redis
import os

# Configuración de Redis
redis_host = os.environ.get("REDIS_HOST", "localhost")  # Valor predeterminado: localhost
redis_port = os.environ.get("REDIS_PORT", 6379)       # Valor predeterminado: 6379
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)

app = FastAPI()
app.title = "Banco de los Alpes"
app.version = "0.0.1"


app.include_router(tarjeta_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip_address = request.client.host  # Obtener la dirección IP del cliente

    # Incrementar el contador de peticiones para esta IP
    redis_key = f"rate_limit:{ip_address}"
    current_count = redis_client.incr(redis_key)

    # Establecer el límite de peticiones y el tiempo de expiración (en segundos)
    limit = 15000  # 5 peticiones por minuto
    expire_time = 6000  # 60 segundos (1 minuto)

    # Configurar la expiración de la clave en Redis si es la primera petición
    if current_count == 1:
        redis_client.expire(redis_key, expire_time)

    # Verificar si se ha excedido el límite
    if current_count > limit:
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"detail": "Demasiadas peticiones. Por favor, inténtelo de nuevo más tarde."},
        )

    # Continuar con la siguiente llamada si no se ha excedido el límite
    response = await call_next(request)
    return response

@app.get('/')
def root():
    return {"id": socket.gethostname()}
