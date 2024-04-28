from fastapi import APIRouter, Depends
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from config.db import get_db
from schema.user_schema import UserCreate
from auth.token import get_current_active_user
from model.book_model import BookModel
from queries.book_queries import get_all_books, get_title_books, get_user_books#, book_not_found
from schema.book_schema import BookRequest, BookResponse

# BOOK Router
book_router = APIRouter(prefix="/books", tags=["Books"] )

# DB Session
session: sessionmaker = Depends(get_db)

# GET ALL BOOKS Route
@book_router.get("/", status_code=200)
async def get_books(user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_books = get_all_books(db)

    return db_books

# GET BOOK BOOKS by TITLE Route
@book_router.get("/{title_id}", status_code=200)
async def get_books_by_title(title_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    title_books = get_title_books(title_id, db)
    
    return title_books

# GET BOOK BOOKS by USER Route
@book_router.get("/{user_id}", status_code=200)
async def get_books_by_user(user_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    user_books = get_user_books(user_id, db)

    return user_books

# CREATE NEW BOOK Route
@book_router.post("/new_book", status_code=201, response_model=BookResponse)
async def create_book(new_book: BookRequest, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_book = BookModel(**new_book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book
"""
# UPDATE BOOK Router
@book_router.put("/update/{title_id}/{user_id}", response_model=BookResponse)
async def update_book(title_id: int, user_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], updated_book: BookRequest, db=Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        book_not_found()
    db_book.title_id = updated_book.title_id
    db_book.ownner_id = updated_book.owner_id
    db.commit()
    db.refresh(db_book)

    return db_book

# DELETE BOOK Router
@book_router.delete("/delete/{book_id}")
async def delete_book(book_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db=Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        book_not_found
    db.delete(db_book)
    db.commit()

    return {"message": "Book deleted successfully"}
"""