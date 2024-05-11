from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer

from authlib.integrations.starlette_client import OAuth

auth_router = APIRouter()

oauth = OAuth()
oauth.register(
    name='auth0',
    client_id='uzjiRjQpkLjHZoIKvUVywVdnpiZG884A',
    client_secret='Avk-wIMQJDqwFbkKS-hhTN-TypT8PJ0JiWBtQEzxxeYCf3JcrKbkNk4OYQxnVFCM',
    server_metadata_url='https://dev-buva6xsj816cpyze/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)

@auth_router.get("/login", tags = ['autenticacion'])
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return oauth.auth0.authorize_redirect(request, redirect_uri)

@auth_router.get("/auth", tags = ['autenticacion'])
async def auth(request: Request):
    token = await oauth.auth0.authorize_access_token(request)
    user = await oauth.auth0.parse_id_token(request, token)
    return {"user_id": user['sub'], "user_email": user['email']}