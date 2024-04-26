from pydantic import BaseModel
from datetime import datetime

# Pydantic Request Schema
class BookRequest(BaseModel):
    title_id: int
    owner_id: int

# Pydantic Response Schema
class BookResponse(BookRequest):
    created_at: datetime
    updated_at: datetime
    #quantity: int
