from pydantic import BaseModel
from datetime import datetime
# Pydantic Request Schema
class UserRequest(BaseModel):
    username: str
    email: str

# Pydantic Response Schema
class UserResponse(UserRequest):
    id: int
    created_at: datetime
    logged_in: bool = False