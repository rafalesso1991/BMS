from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from config.db import get_db
from sqlalchemy.orm import sessionmaker
from datetime import timedelta
from auth.token import SECRET_KEY
from auth.hash import ALGORITHM, verify_hashed_password
from auth.token import create_token, oauth2_scheme
from model.user_model import UserModel
from schema.title_schema import TitleResponse
from queries.title_queries import get_all_titles, get_title
from schema.user_schema import UserCreate, UserResponse
from jose import jwt, JWTError
from pydantic import BaseModel
from queries.user_queries import obtain_user
from typing import Annotated

# AUTORIZATHION ROUTER
auth_router = APIRouter(prefix="/auth", tags=["Auth"])

session: sessionmaker = Depends(get_db)


fake_users_db = [ 
    {
        "username": "wadewilson",
        "email": "deadpool@marvel.com",
        "hashed_password": "chimichangas4life",
        "admin": False,
    },
    {
        "username": "logan",
        "email": "wolverine@marvel.com",
        "hashed_password": "1mcanadian",
        "admin": False,
    },
]

class Token(BaseModel):
    access_token: str
    token_type: str




# Garantizar q exista el usuario "wadewilson" y q su contraseña sea correcta
def authenticate_user(db, username, password):
    user = obtain_user(db, username)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Authentication Credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if not verify_hashed_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user
# Comprobar q el usuario q nos mando el token existe
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db = session):
    try:
        token_decode = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        username = token_decode.get("sub")
        if username == None:
            raise HTTPException (
                status_code=401,
                detail='Invalid credential',
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException (
            status_code=401,
            detail='Invalid credential',
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    user = obtain_user(db, username)
    if not user:
        raise HTTPException (
            status_code=401,
            detail='Invalid credential',
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user

# Garantizar q nuestro token de usuario no haya expirado
def get_current_active_user(user: UserCreate = Depends(get_current_user)):
    if user.admin:
        raise HTTPException (
            status_code=400,
            detail='Inactive user'
        )
    return user

@auth_router.get("/{title_id}", status_code=200)
async def get_title_by_id(title_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    if not user:
        raise HTTPException (
            status_code=400,
            detail='Inactive user'
        )
    db_title = get_title(title_id, db)

    return db_title

@auth_router.get("/wadewilson", response_model=UserResponse)
async def user(user: Annotated[UserCreate, Depends(get_current_active_user)], db = session): # Depends es una inyección d dependencias, consiste en una función q se va a ejecutar cuando se ingrese a la ruta
    user_data = obtain_user(db, user.username)

    return user_data


# Los datos p / la autentización tienen q pasar 1ro x la ruta 'token'
@auth_router.post("/token")
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db = session
    ) -> Token :
    form_data
    
    user = authenticate_user(db, form_data.username, form_data.password)
    print(user)
    print(form_data.username)
    access_token_expires = timedelta(minutes=1)
    print(access_token_expires)
    token = create_token({"sub": user.username}, access_token_expires) # "sub" es parte d la implementación d oauth2 p / los sistemas q utilizan jwt
    return {
        "access_token": token,
        "token_type": "bearer"
    }
    # Keremos q nos retorne el 'token' p / pasarlo a la ruta "/current_user"