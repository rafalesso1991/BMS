from fastapi import APIRouter, Depends, HTTPException
from config.db import get_db
from model.user_model import UserModel
from schema.user_schema import UserRequest, UserResponse, UserCreate
from router.auth_router import generate_hash
from sqlalchemy.orm import sessionmaker

# Users Router
user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Get All Users
@user_router.get("/")
async def get_users(db=Depends(get_db)):

    db_users = db.query(UserModel).all()
    return db_users

# Create User
@user_router.post("/signup", status_code=201, response_model=UserResponse)
async def create_user(new_user: UserCreate, db: sessionmaker = Depends(get_db)):
    hashed_pass = generate_hash(new_user.password)
    db_user = UserModel(username=new_user.username, email=new_user.email, hashed_password=hashed_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
   
    return UserResponse(id=db_user.id, 
                         username=db_user.username, 
                         email=db_user.email,
                         updated_at=db_user.updated_at,
                         created_at=db_user.created_at)

# Get User
@user_router.get("/{user_id}", status_code=201, response_model=UserResponse)
async def get_user(user_id: int, db: sessionmaker = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Update User
@user_router.put("/{user_id}", status_code=201, response_model=UserResponse)
async def update_user(user_id: int, updated_user: UserRequest, db=Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = updated_user.username
    db_user.desc = updated_user.description
    db_user.ownner_id = updated_user.owner_id
    db.commit()
    db.refresh(db_user)
    return db_user

# Delete User
@user_router.delete("/{user_id}", status_code=201)
async def delete_user(user_id: int, db=Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}