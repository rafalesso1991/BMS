from fastapi import HTTPException
from model.user_model import UserModel

# OBTAIN USER FUNCTION
def obtain_user(db, username: str):
    db_user = db.query(UserModel).filter(UserModel.username == username).first()
    return db_user

# GET ALL USERS
def get_all_users(db):
    db_users = db.query(UserModel).all()
    return db_users

# GET USER by ID
def get_user(user_id: int, db):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    return db_user

# HTTP EXCEPTION "USER NOT FOUND"
def user_not_found():
    raise HTTPException(status_code=404, detail="User not found")

# HTTP EXCEPTION "USERNAME ALREADY REGISTERED"
def username_is_taken(username: str, db):
    repeated_user = db.query(UserModel).filter(UserModel.username == username).first()
    if repeated_user is not None:
        raise HTTPException(status_code=409, detail="A user with that name already exists")

# HTTP EXCEPTION "EMAIL ALREADY REGISTERED"
def email_is_taken(username: str, db):
    repeated_email = db.query(UserModel).filter(UserModel.email == username).first()
    if repeated_email is not None:
        raise HTTPException(status_code=409, detail="A user with that email already exists")