from fastapi import APIRouter, Depends
from config.db import get_db
from model.user_model import UserModel
from provider.hash_provider import generate_hash
from schema.user_schema import UserModel
from schema.user_schema import UserCreate, UserResponse
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter()

@auth_router.post('/register', status_code=201, response_model=UserResponse)
def create_user(new_user: UserCreate, db: sessionmaker = Depends(get_db)):
	db_user = UserModel(**new_user.dict())
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user