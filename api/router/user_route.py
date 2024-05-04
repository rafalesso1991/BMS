from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import sessionmaker
from config.db import get_db
from typing import Annotated, List
from schema.user_schema import UserRequest, UserResponse, UserCreate
from auth.token import check_token
from query.user_query import get_all_users, get_user
from model.user_model import User
from auth.hash import generate_hash
from util.exceptions import user_not_found_exception, duplicated_username_exception, duplicated_email_exception

# USER ROUTER
user_router = APIRouter(prefix = "/users", tags = ["Users"])

# DB SESSION
session: sessionmaker = Depends(get_db)

# GET ALL USERS Router
@user_router.get("/", status_code = status.HTTP_200_OK)
async def get_users(token: Annotated[List[UserCreate], Depends(check_token)], db = session):
    db_users = get_all_users(db)
    return db_users

# CREATE NEW USER Router
@user_router.post("/signup", status_code = status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(new_user: UserCreate, db = session):
    hashed_pass = generate_hash(new_user.password)
    db_user = User(username=new_user.username,
                   email=new_user.email,
                   hashed_password=hashed_pass)
    db_users = get_all_users(db)
    for user in db_users:
        if new_user.username == user.username:
            raise duplicated_username_exception
        if new_user.email == user.email:
            raise duplicated_email_exception
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
   
    return UserResponse(id = db_user.id, 
                        username = db_user.username, 
                        email = db_user.email)

# UPDATE USER Route
@user_router.put("/update/{user_id}", status_code = status.HTTP_200_OK, response_model=UserResponse)
async def update_user(user_id: int, token: Annotated[str, Depends(check_token)], updated_user: UserRequest, db = session):
    db_user = get_user(user_id, db)
    if not db_user:
        user_not_found_exception
    db_user.username = updated_user.username
    db_user.email = updated_user.email
    db.commit()
    db.refresh(db_user)

    return db_user

# DELETE USER Route
@user_router.delete("/delete/{user_id}", status_code = status.HTTP_200_OK)
async def delete_user(user_id: int, token: Annotated[str, Depends(check_token)], db = session):
    db_user = get_user(user_id, db)
    if not db_user:
        user_not_found_exception
    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully"}
