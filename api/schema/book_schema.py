from pydantic import BaseModel

# Pydantic Request Schema
class BookRequest(BaseModel):
    title: str
    description: str
    owner: int

# Pydantic Response Schema
class BookResponse(BookRequest):
    id: int
