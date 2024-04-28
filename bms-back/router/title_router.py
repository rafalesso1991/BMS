from fastapi import APIRouter, Depends
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from config.db import get_db
from schema.user_schema import UserCreate
from auth.token import get_current_active_user
from queries.title_queries import get_all_titles, get_title, get_user_titles#, get_name_titles, get_author_titles, get_genre_titles, get_year_titles
from schema.title_schema import TitleResponse, TitleRequest
from model.title_model import TitleModel
from handler.title_handler import title_not_found

# TITLE Router
title_router = APIRouter(prefix="/titles", tags=["Titles"])

# DB Session
session: sessionmaker = Depends(get_db)

# USER Session
user: Annotated[UserCreate, Depends(get_current_active_user)]

# GET ALL TITLES Route
@title_router.get("/", status_code=200)
async def get_titles(user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_titles = get_all_titles(db)

    return db_titles

@title_router.get("/{title_id}", status_code=200)
async def get_title_by_id(title_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_title = get_title(title_id, db)

    return db_title
"""
# GET TITLE by NAME Route
@title_router.get("/by_name/{title_name}", status_code=200)
async def get_title_by_name(title_name: str, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_title = get_name_titles(title_name, db)

    return db_title

# GET TITLE by AUTHOR Route
@title_router.get("/by_author/{title_author}", status_code=200)
async def get_title_by_author(title_author: str, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_title = get_author_titles(title_author, db)

    return db_title

# GET TITLE by GENRE Route
@title_router.get("/by_genre/{title_genre}", status_code=200)
async def get_titles_by_genre(title_genre: str, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    genre_titles = get_genre_titles(title_genre, db)

    return genre_titles

# GET TITLE by YEAR Route
@title_router.get("/by_year/{title_year}", status_code=200)
async def get_title_by_year(title_year: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    year_title = get_year_titles(title_year, db)

    return year_title
"""
# GET TITLE by USER Route
@title_router.get("/by_user/{user_id}", status_code=200)
async def get_titles_by_user(user_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    user_titles = get_user_titles(user_id, db)

    return user_titles

# CREATE TITLE Route
@title_router.post("/new_title/{title_id}", status_code=201, response_model=TitleResponse)
async def create_title(new_title: TitleRequest, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_title = TitleModel(**new_title.dict())
    db.add(db_title)
    db.commit()
    db.refresh(db_title)

    return db_title

# UPDATE TITLE Route
@title_router.put("/update/{title_id}", response_model=TitleResponse)
async def update_title(title_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], updated_title: TitleRequest, db = session):
    db_title = get_title(title_id, db)
    if not db_title:
        title_not_found()
    db_title.name = updated_title.name
    db_title.author = updated_title.author
    db_title.genre = updated_title.genre
    db_title.year = updated_title.year
    db.commit()
    db.refresh(db_title)

    return db_title

# DELETE TITLE
@title_router.delete("/delete/{title_id}")
async def delete_title(title_id: int, user: Annotated[UserCreate, Depends(get_current_active_user)], db = session):
    db_title = get_title(title_id, db)
    if not db_title:
        title_not_found()
    db.delete(db_title)
    db.commit()

    return {"message": "Title deleted successfully"}
