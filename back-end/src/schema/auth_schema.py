from pydantic import BaseModel
from datetime import datetime
# Pydantic Request Schema
class AuthRequest(BaseModel):
    username: str
    password: str
# Pydantic Response Schema
class AuthResponse(AuthRequest):
    id: int
    access_token: str
    token_type: str
    created_at: datetime
    logged_in: bool = False