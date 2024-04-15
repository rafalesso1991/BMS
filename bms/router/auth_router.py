from fastapi import APIRouter, Depends, HTTPException
from config.db import get_db
from schema.auth_schema import AuthRequest, AuthResponse
from sqlalchemy.orm import sessionmaker
from datetime import timedelta
from auth.hash import ALGORITHM, generate_hash, verify_hashed_password
from auth.token import create_token
from queries.user_queries import obtain_user

# AUTORIZATHION ROUTER
auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# LOGIN ROUTER
@auth_router.post("/login")
async def login(credentials: AuthRequest, db: sessionmaker = Depends(get_db)):
    user = obtain_user(db, credentials.username)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if not verify_hashed_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=30)
    token = create_token({"sub": user.username}, access_token_expires)
    """
    Ruta para loguear el usuario.

    Args: credeciales (user, pass)

    Returns: String, un JTW
    """
    return AuthResponse(id=user.id,
                        username=credentials.username,
                        password=generate_hash(credentials.password),
                        access_token=token, 
                        token_type="bearer",
                        created_at=user.created_at,
                        updated_at=user.updated_at,
                        logged_in=False
    )
    """
    return {
        "access_token": access_token_jwt,
        "token_type": "bearer"
    }
    """