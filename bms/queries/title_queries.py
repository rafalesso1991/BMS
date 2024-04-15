from fastapi import HTTPException
from model.book_model import BookModel
from model.title_model import TitleModel

# GET ALL TITLES
def get_all_titles(db):
    db_titles = db.query(TitleModel).all()
    return db_titles

# GET TITLE by ID
def get_title(title_id: int, db):
    db_title = db.query(TitleModel).filter(TitleModel.id == title_id).first()
    return db_title

# GET TITLES by USER
def get_user_titles(user_id: int, db):
    user_titles = db.query(TitleModel).join(BookModel).filter(BookModel.owner_id == user_id).all()
    return user_titles

# HTTP EXCEPTION "TITLE NOT FOUND"
def title_not_found():
    raise HTTPException(status_code=404, detail="Title not found")