from fastapi import APIRouter, Depends
from config.db import get_db
from model.user_model import UserModel
from provider.hash_provider import generate_hash, verify_hash
from model.user_model import UserModel
from schema.user_schema import UserCreate, UserResponse
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter()

@auth_router.post('/register', status_code=201, response_model=UserResponse)
def create_user(new_user: UserCreate, db: sessionmaker = Depends(get_db)):
	db_user = UserModel(**new_user.dict())
	db.add(db_user)
	hash_password = generate_hash(new_user.password)
	print(new_user.password)
	print(hash_password)
	print(verify_hash(new_user.password, hash_password))
	db.commit()
	db.refresh(db_user)
	return db_user