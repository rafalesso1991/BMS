from fastapi import APIRouter, Depends
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from auth.token import authenticate_user, create_token
from config.db import get_db
from schema.auth_schema import Token

# AUTORIZATHION ROUTER
auth_router = APIRouter(prefix="/auth", tags=["Auth"])

session: sessionmaker = Depends(get_db)

# Los datos p / la autentización tienen q pasar 1ro x la ruta '/token'
@auth_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db = session) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=1)
    token = create_token({"sub": user.username}, access_token_expires) # "sub" es parte d la implementación d oauth2 p / los sistemas q utilizan jwt
    return {
        "access_token": token,
        "token_type": "bearer"
    }
