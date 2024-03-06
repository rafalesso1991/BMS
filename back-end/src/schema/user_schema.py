from pydantic import BaseModel
from datetime import datetime
# Pydantic Request Schema
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
# Pydantic Response Schema
class UserResponse(UserCreate):
    id: int
    created_at: datetime