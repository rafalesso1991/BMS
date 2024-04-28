from fastapi import APIRouter, Depends
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from config.db import get_db
from schema.user_schema import UserCreate, UserResponse, UserRequest
from auth.token import get_current_active_user
from queries.user_queries import get_all_users, get_user
from handler.user_handler import username_is_taken, email_is_taken, user_not_found
from auth.hash import generate_hash
from model.user_model import UserModel

# Users Router
user_router = APIRouter(prefix="/users", tags=["Users"])

# DB Session
session: sessionmaker = Depends(get_db)

# GET ALL USERS Router
@user_router.get("/", status_code=200)
async def get_users(user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_users = get_all_users(db)

    return db_users

# GET USER Router
@user_router.get("/{user_id}", status_code=200)
async def get_username(user_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_user = get_user(user_id, db)

    return db_user

# CREATE NEW USER Router
@user_router.post("/signup", status_code=201, response_model=UserResponse)
async def create_user(new_user: UserCreate, db = session):
    username_is_taken(new_user.username, db)
    email_is_taken(new_user.email, db)
    hashed_pass = generate_hash(new_user.password)
    db_user = UserModel(username=new_user.username,
                        email=new_user.email,
                        hashed_password=hashed_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
   
    return UserResponse(id=db_user.id, 
                        username=db_user.username, 
                        email=db_user.email,
                        created_at=db_user.created_at,
                        updated_at=db_user.updated_at)

# UPDATE USER Route
@user_router.put("/update/{user_id}", status_code=200, response_model=UserResponse)
async def update_user(user_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], updated_user: UserRequest, db = session):
    db_user = get_user(user_id, db)
    if not db_user:
        user_not_found()
    db_user.username = updated_user.username
    db_user.email = updated_user.email
    db.commit()
    db.refresh(db_user)

    return db_user

# DELETE USER Route
@user_router.delete("/delete/{user_id}", status_code=200)
async def delete_user(user_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_user = get_user(user_id, db)
    if not db_user:
        user_not_found()
    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully"}