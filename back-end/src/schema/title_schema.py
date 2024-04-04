from pydantic import BaseModel
from typing import Optional
from datetime import datetime
# Pydantic Request Schema
class BookRequest(BaseModel):
    name: str
    author: Optional[str]
    genre: Optional[str]
    year: Optional[int]
# Pydantic Response Schema
class BookResponse(BookRequest):
    id: int
    created_at: datetime
    updated_at: datetime
