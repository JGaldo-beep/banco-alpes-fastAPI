#from middlewares.error_handler import ErrorHandler
from fastapi.responses import JSONResponse
from router.auth import auth_router
from router.tarjeta import tarjeta_router
from router.solicitud import solicitud_router
from config.database import engine, Base
from router.usuario import usuario_router
from fastapi import Depends, FastAPI, HTTPException
from authlib.integrations.starlette_client import OAuth

import socket

app = FastAPI()
app.title = 'Banco de los Alpes'
app.version = "0.0.1"

#app.add_middleware(ErrorHandler)
app.include_router(tarjeta_router)
app.include_router(auth_router)
app.include_router(solicitud_router)
app.include_router(usuario_router)

oauth = OAuth()
oauth.register(
    name='auth0',
    client_id='uzjiRjQpkLjHZoIKvUVywVdnpiZG884A',
    client_secret='Avk-wIMQJDqwFbkKS-hhTN-TypT8PJ0JiWBtQEzxxeYCf3JcrKbkNk4OYQxnVFCM',
    server_metadata_url='https://dev-buva6xsj816cpyze/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {"id": socket.gethostname()}

##Auth 0
@app.get("/profile")
async def profile(token: str = Depends(oauth.authenticator(['auth0']))):
    user = token.user
    return {"user_id": user.get('sub'), "user_email": user.get('email')}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )