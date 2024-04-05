from pydantic import BaseModel
from datetime import datetime
# Pydantic Request Schema

    
class UserRequest(BaseModel):
    username: str
    email: str


class UserCreate(UserRequest):
    password: str
    
    
class UserResponse(UserRequest):
    id: int
    admin: bool = False
    created_at: datetime
    updated_at: datetime
    