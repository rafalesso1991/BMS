from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from config.db import get_db
from model.user_model import UserModel
from schema.auth_schema import AuthRequest, AuthResponse
from sqlalchemy.orm import sessionmaker
from typing import Union
from datetime import datetime, timedelta
from jose import jwt, JWTError

# AUTORIZATHION ROUTER
auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)
# PASSWORD BEARER AUTORIZATHION SCHEMA --> indica la ruta dnde vamos a recibir el token
oauth2_scheme = OAuth2PasswordBearer("/login")
# PASSWORD ENCRYPTER
password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
# TOKEN PARAMS
SECRET_KEY = "secret"
ALGORITHM = "HS256"

# HASH GENERATOR FUNCTION
def generate_hash(plain_password):
	return password_context.hash(plain_password)
# PASSWORD VERIFIER FUNCTION
def verify_password(form_password, password):
	return password_context.verify(form_password, password)# True or False
# OBTAIN USER FUNCTION
def obtain_user(db, username: str):
    db_user = db.query(UserModel).filter(UserModel.username == username).first()
    return db_user
# CREATE TOKEN FUNCTION
def create_token(data: dict, time_expire: Union[datetime, None] = None):
    data_copy = data.copy()
    if time_expire is None:
        expires = datetime.utcnow() + timedelta(minutes=15)
    else:
        expires = datetime.utcnow() + time_expire
    data_copy.update({"exp": expires})
    token_jwt = jwt.encode(data_copy, key=SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

# ROOT ROUTER
@auth_router.get("/")
def root(db: sessionmaker = Depends(get_db)):
    print(verify_password("asdasd", "$2b$12$KWzaJiSNcwNtlDEvYm/R4uYAh3Z.tc5M62ooSJzcwk1AX2WBZGg.q"))
# LOGIN FORM ROUTER
@auth_router.post("/login", status_code=201)
async def login(credentials: AuthRequest, db: sessionmaker = Depends(get_db)):
    user = obtain_user(db, credentials.username)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=30)
    token = create_token({"sub": user.username}, access_token_expires)
    return AuthResponse(id=user.id,
                        username=credentials.username,
                        password=generate_hash(credentials.password),
                        access_token=token, 
                        token_type="bearer",
                        created_at=user.created_at,
                        logged_in=user.logged_in
    )
    id: int
    access_token: str
    token_type: str
    created_at: datetime
    logged_in: bool = False
"""
from fastapi import APIRouter, Depends
from config.db import get_db
from model.auth_model import AuthModel
from provider.hash_provider import generate_hash, verify_hash
from provider.token_provider import oauth2_scheme
from model.auth_model import AuthModel
from schema.auth_schema import AuthCreate, AuthResponse
from sqlalchemy.orm import sessionmaker

@auth_router.get('/token/')
async def get_users(token: str = Depends(oauth2_scheme)):
	return {"token": token}

@auth_router.post('/register', status_code=201, response_model=UserResponse)
async def create_user(new_user: UserCreate, db: sessionmaker = Depends(get_db)):
	db_user = UserModel(**new_user.dict())
	db.add(db_user)
	hashed_password = generate_hash(new_user.password)
	print(new_user.password)
	print(hashed_password)
	print(verify_hash(new_user.password, hashed_password))
	db.commit()
	db.refresh(db_user)
	return {"message": "User registered successfully"}
"""