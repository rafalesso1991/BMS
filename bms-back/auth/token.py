from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from config.db import get_db
from sqlalchemy.orm import sessionmaker
from typing import Annotated, Union
from datetime import datetime, timedelta
from jose import jwt, JWTError
from .hash import ALGORITHM, verify_hashed_password
from handler.auth_handler import invalid_credentials, token_expired
from queries.user_queries import get_user
from schema.user_schema import UserCreate

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token") # El único parámetro es la ruta del formulario en dnde se van a enviar los datos solicitados

SECRET_KEY = "secret"

session: sessionmaker = Depends(get_db)

# Garantizar q exista el usuario ingresado y q su contraseña sea correcta
def authenticate_user(db, username, password):
    user = get_user(db, username)
    if not user:
        invalid_credentials()
    if not verify_hashed_password(password, user.hashed_password):
        invalid_credentials()

    return user

# Crear un JWT con tiempo d expiración para la ruta "/token"
def create_token(data: dict, time_expire: Union[datetime, None] = None):
    data_copy = data.copy()
    if time_expire is None:
        expires = datetime.utcnow() + timedelta(minutes=15)
    else:
        expires = datetime.utcnow() + time_expire
    data_copy.update({"exp": expires})
    token_jwt = jwt.encode(data_copy, key=SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

# Comprobar q el usuario q nos mando el token existe
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db = session):
    try:
        token_decode = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        username = token_decode.get("sub")
        if username == None:
            invalid_credentials()
    except JWTError:
        token_expired()
    
    user = get_user(db, username)
    if not user:
        invalid_credentials()

    return user

# Garantizar q nuestro token de usuario no haya expirado
def get_current_active_user(user: UserCreate = Depends(get_current_user)):
    if user.admin:
        token_expired()
    return user
