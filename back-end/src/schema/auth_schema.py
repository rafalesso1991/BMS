from pydantic import BaseModel
# Pydantic Request Schema
class LoginData(BaseModel):
    email: str
    password: str
# Pydantic Response Schema
class LoginSuccess(BaseModel):
    user: str
    access_token: str