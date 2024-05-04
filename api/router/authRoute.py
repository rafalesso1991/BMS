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


# AUTHENTICATE CREDENTIALS
def authenticate_user(username, password, db):
    user = get_user(username, db)
    if not user:
        raise credentials_exception
    if not verify_hashed_password(password, user.hashed_password):
        raise credentials_exception
    return user



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
