from pydantic import BaseModel

# Pydantic Response Schema
class Token(BaseModel):
    access_token: str
    token_type: str
