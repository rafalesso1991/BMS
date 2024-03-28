from pydantic import BaseModel
from typing import Optional
from datetime import datetime
# Pydantic Request Schema
class BookRequest(BaseModel):
    title: str
    description: Optional[str]
    owner_id: int
    token: str
# Pydantic Response Schema
class BookResponse(BookRequest):
    id: int
    created_at: datetime