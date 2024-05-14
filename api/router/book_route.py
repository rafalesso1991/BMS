from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import sessionmaker
from config.db import get_db
from typing import Annotated
from schema.book_schema import BookRequest, BookResponse
from auth.token import check_token
from query.book_query import get_all_books, get_owned_books, get_book
from query.user_query import get_user
from utils import book_not_found_exception
from model.book_model import Book

# BOOK ROUTER
book_router = APIRouter(prefix = "/books", tags = ["Books"])

# DB SESSION
session: sessionmaker = Depends(get_db)

# GET ALL BOOKS
@book_router.get("/", status_code = status.HTTP_200_OK)
async def get_books(token: Annotated[str, Depends(check_token)], db = session):
    db_books = get_all_books(db)

    return db_books

# GET OWNED BOOKS
@book_router.get("/my_books", status_code = status.HTTP_200_OK)
async def get_books_by_owner(user: Annotated[str, Depends(check_token)], db = session):
    db_user = get_user(user, db)
    user_books = get_owned_books(db_user.id, db)

    return user_books

# CREATE BOOK
@book_router.post("/new_book", status_code = status.HTTP_201_CREATED, response_model=BookResponse)
async def create_book(new_book: BookRequest, user: Annotated[str, Depends(check_token)], db = session):
    db_user = get_user(user, db)
    book_data = new_book.dict()  # Convert request to dict
    book_data["owner"] = db_user.id
    db_book = Book(**book_data)    
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return BookResponse(id=db_book.id, **book_data)

# UPDATE BOOK
@book_router.put("/update/{book_id}", status_code = status.HTTP_200_OK, response_model=BookResponse)
async def update_book(book_id: int, user: Annotated[str, Depends(check_token)], updated_book: BookRequest, db = session):
    db_book = get_book(book_id, db)
    if not db_book:
        raise book_not_found_exception
    db_book.title = updated_book.title
    db_book.description = updated_book.description
    db.commit()
    db.refresh(db_book)

    return db_book

# DELETE BOOK
@book_router.delete("/delete/{book_id}", status_code = status.HTTP_200_OK)
async def delete_title(book_id: int, user: Annotated[str, Depends(check_token)], db = session):
    db_book = get_book(book_id, db)
    if not db_book:
        raise book_not_found_exception
    db.delete(db_book)
    db.commit()

    return {"message": "Book deleted successfully"}
