from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import sessionmaker
from config.db import get_db
from model.user_model import UserModel
from schema.user_schema import UserRequest, UserResponse, UserCreate
from auth.hash import generate_hash
from queries.user_queries import get_all_users, get_user, user_not_found, username_is_taken, email_is_taken
from queries.title_queries import get_user_titles
from typing import Annotated, List
from .auth_router import get_current_active_user
from auth.token import check_token
from handler.credentials import credentials_exception


# Users Router
user_router = APIRouter(prefix="/users", tags=["Users"])

# DB Session
session: sessionmaker = Depends(get_db)

def get_all_users_secured(db_users: Annotated[List[UserCreate], Depends(check_token)],db):
    
    return [] 

# GET ALL USERS Router
@user_router.get("/", status_code=200)
async def get_users(token: Annotated[str, Depends(check_token)], db = session):
    db_users = db.query(UserModel).all()
    return db_users

#######################################################################
# GET TITLE by ID Route
@user_router.get("/{username}", status_code=200)
async def get_username(username: str, db = session):
    db_user = get_user(username, db)

    return db_user

# GET BOOK TITLES by USER
@user_router.get("/{user_id}", status_code=200)
async def get_titles_by_user(user_id: int, db = session):
    user_titles = get_user_titles(user_id, db)
    return user_titles

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
async def update_user(user_id: int, updated_user: UserRequest, db = session):
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
async def delete_user(user_id: int, db = session):
    db_user = get_user(user_id, db)
    if not db_user:
        user_not_found()
    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully"}
