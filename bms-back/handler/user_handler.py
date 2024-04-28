from fastapi import HTTPException
from queries.user_queries import get_user
from model.user_model import UserModel

# HTTP EXCEPTION "USER NOT FOUND"
def user_not_found():
    raise HTTPException(status_code=404, detail="User not found")

# HTTP EXCEPTION "DUPLICATED USERNAME"
def username_is_taken(username: str, db):
    duplicated_user = get_user(db, username)
    if duplicated_user is not None:
        raise HTTPException(status_code=409, detail="A user with that name already exists")

# HTTP EXCEPTION "DUPLICATED EMAIL"
def email_is_taken(username: str, db):
    repeated_email = db.query(UserModel).filter(UserModel.email == username).first()
    if repeated_email is not None:
        raise HTTPException(status_code=409, detail="A user with that email already exists")

# HTTP EXCEPTION "TOKEN EXPIRED"
def token_expired():
    raise HTTPException (status_code=440, detail='Session Expired')
