from pydantic import BaseModel

# Pydantic Request Schema
class BookRequest(BaseModel):
    title: str
    description: str

# Pydantic Response Schema
class BookResponse(BookRequest):
    id: int
    owner: int
