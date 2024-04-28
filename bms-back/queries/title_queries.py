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

# GET TITLES by NAME
def get_name_titles(name: str, db):
    name_titles = db.query(TitleModel).filter(TitleModel.name.ilike(name)).all()
    return name_titles

# GET TITLES by AUTHOR
def get_author_titles(author: str, db):
    author_titles = db.query(TitleModel).filter(TitleModel.author.ilike(author)).all()
    return author_titles

# GET TITLES by GENRE
def get_genre_titles(genre: str, db):
    genre_titles = db.query(TitleModel).filter(TitleModel.genre.ilike(genre)).all()
    return genre_titles

# GET TITLES by YEAR
def get_year_titles(year_id: int, db):
    year_titles = db.query(TitleModel).filter(TitleModel.year == year_id).first()
    return year_titles

# GET TITLES by USER
def get_user_titles(user_id: int, db):
    user_titles = db.query(TitleModel).join(BookModel).filter(BookModel.owner_id == user_id).all()
    return user_titles
