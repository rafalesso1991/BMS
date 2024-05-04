from model.book_model import Book
from model.user_model import User

# GET BOOK
def get_book(book_title: str, db):
    db_book = db.query(Book).filter(Book.title == book_title).first()

    return db_book

# GET ALL BOOKS
def get_all_books(db):
    db_books = db.query(Book).all()

    return db_books

# GET OWNED BOOKS
def get_owned_books(user_id: int, db):
    db_books = db.query(Book).join(User).filter(Book.owner == user_id).all()

    return db_books
