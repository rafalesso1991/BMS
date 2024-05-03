from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import sessionmaker
from config.db import get_db
from typing import Annotated, List
from schema.bookSchema import BookRequest, BookResponse
from auth.token import check_token
from query.bookQuery import get_all_books, get_owned_books, get_book
from handler.bookHandler import duplicated_title, book_not_found
from model.bookModel import Book

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
@book_router.get("/by_user/{user_id}", status_code = status.HTTP_200_OK)
async def get_books_by_owner(user_id: int, token: Annotated[str, Depends(check_token)], db = session):
    user_books = get_owned_books(user_id, db)

    return user_books

# CREATE BOOK
@book_router.post("/new_book", status_code = status.HTTP_201_CREATED, response_model=BookResponse)
async def create_book(new_book: BookRequest, token: Annotated[str, Depends(check_token)], db = session):
    db_book = Book(title = new_book.title,
                   description = new_book.description,
                   owner = new_book.owner)
    db_books = get_all_books(db)
    for book in db_books:
        if new_book.title == book.title:
            raise duplicated_title
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book

# UPDATE BOOK
@book_router.put("/update/{book_title}", status_code = status.HTTP_200_OK, response_model=BookResponse)
async def update_book(book_title: str, token: Annotated[str, Depends(check_token)], updated_book: BookRequest, db = session):
    db_book = get_book(book_title, db)
    if not db_book:
        raise book_not_found
    db_book.title = updated_book.title
    db_book.description = updated_book.description
    db.commit()
    db.refresh(db_book)

    return db_book

# DELETE BOOK
@book_router.delete("/delete/{book_title}", status_code = status.HTTP_200_OK)
async def delete_title(book_title: str, token: Annotated[str, Depends(check_token)], db = session):
    db_book = get_book(book_title, db)
    if not db_book:
        raise book_not_found
    db.delete(db_book)
    db.commit()

    return {"message": "Book deleted successfully"}
