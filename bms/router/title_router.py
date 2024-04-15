from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import sessionmaker
from config.db import get_db
from model.title_model import TitleModel
from queries.title_queries import get_all_titles, get_title, get_user_titles, title_not_found
from schema.title_schema import TitleRequest, TitleResponse
from sqlalchemy.orm import Session

# TITLE Router
title_router = APIRouter(prefix="/titles", tags=["Titles"])

# DB Session
session: sessionmaker = Depends(get_db)

# GET ALL TITLES Route
@title_router.get("/", status_code=200)
async def get_titles(db = session):
    db_titles = get_all_titles(db)

    return db_titles

# GET TITLE by ID
@title_router.get("/{title_id}", status_code=200)
async def get_title_by_id(title_id: int, db = session):
    db_title = get_title(title_id, db)

    return db_title

# GET BOOK TITLES by USER
@title_router.get("/{user_id}", status_code=200)
async def get_titles_by_user(user_id: int, db = session):
    user_titles = get_user_titles(user_id, db)
    return user_titles

# CREATE TITLE Route
@title_router.post("/new_title/{title_id}", status_code=201, response_model=TitleResponse)
async def create_title(new_title: TitleRequest, db = session):
    db_title = TitleModel(**new_title.dict())
    db.add(db_title)
    db.commit()
    db.refresh(db_title)

    return db_title

# UPDATE TITLE Route
@title_router.put("/update/{title_id}", response_model=TitleResponse)
async def update_title(title_id: int, updated_title: TitleRequest, db = session):
    db_title = db.query(TitleModel).filter(TitleModel.id == title_id).first()
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
async def delete_title(title_id: int, db = session):
    db_title = db.query(TitleModel).filter(TitleModel.id == title_id).first()
    if not db_title:
        raise HTTPException(status_code=404, detail="Title not found")
    db.delete(db_title)
    db.commit()

    return {"message": "Title deleted successfully"}
