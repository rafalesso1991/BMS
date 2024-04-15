from fastapi import HTTPException
from model.book_model import BookModel

# GET ALL BOOKS
def get_all_books(db):
    db_books = db.query(BookModel).all()
    return db_books

# GET BOOK by TITLE_ID
def get_title_books(title_id: int, db):
    title_books = db.query(BookModel).filter(BookModel.title_id == title_id).all()
    return title_books

# GET BOOK by OWNER_ID
def get_user_books(user_id: int, db):
    user_books = db.query(BookModel).filter(BookModel.owner_id == user_id).all()
    return user_books
"""
# GET BOOK by TITLE_ID
def get_book_title(title_id: int, db):
    book_title = db.query(BookModel).filter(BookModel.title_id == title_id).first()
    return book_title

# GET BOOK by OWNER_ID
def get_book_owner(user_id: int, db):
    book_owner = db.query(BookModel).filter(BookModel.owner_id == user_id).first()
    return book_owner
"""
# HTTP EXCEPTION "BOOK NOT FOUND"
def book_not_found():
    raise HTTPException(status_code=404, detail="Book not found")