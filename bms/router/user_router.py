from fastapi import APIRouter, Depends, HTTPException
from config.db import get_db
from model.book_model import BookModel
from model.title_model import TitleModel
from model.user_model import UserModel
from schema.title_schema import TitleResponse
from schema.user_schema import UserRequest, UserResponse, UserCreate
from router.auth_router import generate_hash
from sqlalchemy.orm import sessionmaker

# Users Router
user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def user_not_found():
    raise HTTPException(status_code=404, detail="User not found")

def username_is_taken(username: str, db: sessionmaker = Depends(get_db)):
    # Query the database for the username
    repeat_user = db.query(UserModel).filter(UserModel.username == username).first()
    return repeat_user is not None

def email_is_taken(username: str, db: sessionmaker = Depends(get_db)):
    # Query the database for the username
    repeat_email = db.query(UserModel).filter(UserModel.email == username).first()
    return repeat_email is not None

# Get All Users
@user_router.get("/")
async def get_users(db=Depends(get_db)):
    db_users = db.query(UserModel).all()
    return db_users

# Create User
@user_router.post("/signup", status_code=201, response_model=UserResponse)
async def create_user(new_user: UserCreate,
                      db: sessionmaker = Depends(get_db)):
    if username_is_taken(new_user.username, db):
        raise HTTPException(status_code=409, detail="A user with that name already exists")
    if email_is_taken(new_user.email, db):
        raise HTTPException(status_code=409, detail="A user with that email already exists")
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

# Get User
@user_router.get("/{user_id}", status_code=201, response_model=UserResponse)
async def get_user(user_id: int, db: sessionmaker = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user: 
        user_not_found()

    return db_user

# GET BOOKS by USER
@user_router.get("/{user_id}", status_code=200, response_model=TitleResponse)
async def get_titles_by_user(user_id: int, db: sessionmaker = Depends(get_db)):
    user_titles = db.query(TitleModel).join(BookModel).filter(BookModel.owner_id == user_id).all()
    print(type(user_titles))
    for user_title in user_titles:
        return user_title

# Update User
@user_router.put("/{user_id}", status_code=201, response_model=UserResponse)
async def update_user(user_id: int, updated_user: UserRequest, db: sessionmaker =Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        user_not_found()
    db_user.username = updated_user.username
    db_user.email = updated_user.email
    db.commit()
    db.refresh(db_user)

    return db_user

# Delete User
@user_router.delete("/{user_id}", status_code=201)
async def delete_user(user_id: int, db: sessionmaker =Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        user_not_found()
    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully"}
