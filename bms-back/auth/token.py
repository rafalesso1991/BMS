from fastapi.security import OAuth2PasswordBearer
from typing import Union
from datetime import datetime, timedelta
from jose import jwt, JWTError
from .hash import ALGORITHM
#
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token") # El único parámetro es la ruta del formulario en dnde se van a enviar los datos solicitados
# TOKEN PARAMS 
SECRET_KEY = "secret"
#
def create_token(data: dict, time_expire: Union[datetime, None] = None):
    data_copy = data.copy()
    if time_expire is None:
        expires = datetime.utcnow() + timedelta(minutes=15)
    else:
        expires = datetime.utcnow() + time_expire
    data_copy.update({"exp": expires})
    token_jwt = jwt.encode(data_copy, key=SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt
