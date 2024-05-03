from fastapi import APIRouter, Depends # Depends es una inyección d dependencias, consiste en una función q se va a ejecutar cuando se ingrese a la ruta
from sqlalchemy.orm import sessionmaker
from config.db import get_db
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from auth.token import SECRET_KEY
from auth.hash import ALGORITHM, verify_hashed_password
from auth.token import create_token, oauth2_bearer
from schema.userSchema import UserCreate, UserResponse
from jose import jwt, JWTError
from query.userQuery import get_user
from typing import Annotated
from handler.authHandler import credentials_exception, inactive_user

# AUTORIZATHION ROUTER
auth_router = APIRouter(prefix="/auth", tags=["Auth"])

session: sessionmaker = Depends(get_db)

import logging

logger = logging.getLogger('foo-logger')

# AUTHENTICATE CREDENTIALS
def authenticate_user(username, password, db):
    user = get_user(username, db)
    if not user:
        raise credentials_exception
    if not verify_hashed_password(password, user.hashed_password):
        raise credentials_exception
    return user

# Comprobar q el usuario q nos mando el token existe
def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db = session):
    try:
        token_decode = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        username = token_decode.get("sub")
        if username == None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user(username, db)
    if not user:
        raise credentials_exception
    return user

# Garantizar q nuestro token de usuario no haya expirado
def get_current_active_user(user: UserCreate = Depends(get_current_user)):
    if user.active:
        raise inactive_user
    return user

@auth_router.get("/current_user", status_code=200, response_model=UserResponse)
async def get_current_user(username: str, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    if not user:
        raise inactive_user
    db_user = get_user(username, db)

    return db_user

@auth_router.get("/myProfile", response_model=UserResponse)
async def user(user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    user_data = get_user(user.username, db)

    return user_data

# Los datos p / la autentización tienen q pasar 1ro x la ruta 'token'
@auth_router.post("/token")
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db = session
    ):
    
    user = authenticate_user(form_data.username, form_data.password, db)
    access_token_expires = timedelta(minutes=15)
    token = create_token({"sub": user.username}, access_token_expires) # "sub" es parte d la implementación d oauth2 p / los sistemas q utilizan jwt
    return {
        "access_token": token,
        "token_type": "bearer",
        'success': 'true'
    } # Keremos q nos retorne el 'token' p / pasarlo a la ruta "/current_user"
