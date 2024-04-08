from pydantic import BaseModel
from datetime import datetime

# Pydantic Request Schema
class UserRequest(BaseModel):
    username: str
    email: str

# Pydantic Request Schema for Create User
class UserCreate(UserRequest):
    password: str

# Pydantic Response Schema
class UserResponse(UserRequest):
    id: int
    admin: bool = False
    created_at: datetime
    updated_at: datetime
