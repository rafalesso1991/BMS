from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic Request Schema
class TitleRequest(BaseModel):
    name: str
    author: Optional[str]
    genre: Optional[str]
    year: Optional[int]

# Pydantic Response Schema
class TitleResponse(TitleRequest):
    id: int
    created_at: datetime
    updated_at: datetime
