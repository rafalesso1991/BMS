from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Pydantic Request Schema
class TitleRequest(BaseModel):
    name: str
    author: Optional[str]
    genre: Optional[str]
    year: Optional[int] = Field(..., gt=0, le=datetime.now().year)

# Pydantic Response Schema
class TitleResponse(TitleRequest):
    id: int
    created_at: datetime
    updated_at: datetime
