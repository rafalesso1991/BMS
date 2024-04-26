from pydantic import BaseModel, EmailStr
from datetime import datetime

# Pydantic Request Schema
class UserRequest(BaseModel):
    username: str
    email: EmailStr
    admin: bool = False # disabled: bool

# Pydantic Request Schema for Create User
class UserCreate(UserRequest):
    password: str # hashed_password: str

# Pydantic Response Schema
class UserResponse(UserRequest):
    id: int
    created_at: datetime
    updated_at: datetime
