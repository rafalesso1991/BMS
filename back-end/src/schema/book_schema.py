from pydantic import BaseModel
from typing import Optional
from datetime import datetime
# Pydantic Request Schema
class BookCreate(BaseModel):
    name: str
    description: Optional[str]
    owner_id: int
# Pydantic Response Schema
class BookResponse(BookCreate):
    id: int
    created_at: datetime