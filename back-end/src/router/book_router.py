from fastapi import APIRouter, Depends, HTTPException
from config.db import get_db
from model.book_model import BookModel
from schema.book_schema import BookRequest, BookResponse
from sqlalchemy.orm import Session

# Books Router
book_router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

# Get All Books
@book_router.get("/")
async def get_books(db=Depends(get_db)):
    db_books = db.query(BookModel).all()# db_books = conexión con db q lista (en formato BaseModel) *todos
    return db_books

# Create Book
@book_router.post("/{book_id}", status_code=201, response_model=BookResponse)
async def create_book(new_book: BookRequest, db: Session = Depends(get_db)):
    db_book = BookModel(**new_book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Get Book
@book_router.get("/{book_id}", status_code=201, response_model=BookResponse)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()# db lista en formato BaseModel y filtra para q el id d la request es igual al id de la db) y devuelve el 1er resultado
    if not db_book:
        raise HTTPException(status_code=404, detail="User not found")
    return db_book

# Update Book
@book_router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, updated_book: BookRequest, db=Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title_id = updated_book.title_id
    db_book.ownner_id = updated_book.owner_id
    db.commit()
    db.refresh(db_book)
    return db_book

# Delete Book
@book_router.delete("/{book_id}")
async def delete_book(book_id: int, db=Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}