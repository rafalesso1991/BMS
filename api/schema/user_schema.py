from pydantic import BaseModel, EmailStr

# Pydantic Request Schema
class UserRequest(BaseModel):
    username: str
    email: EmailStr
    active: bool = False

# Pydantic Request Schema for CREATE
class UserCreate(UserRequest):
    password: str

# Pydantic Response Schema
class UserResponse(UserRequest):
    id: int
