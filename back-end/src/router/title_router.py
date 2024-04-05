from fastapi import APIRouter, Depends, HTTPException
from config.db import get_db
from model.title_model import TitleModel
from schema.title_schema import TitleRequest, TitleResponse
from sqlalchemy.orm import Session

# Title Router
title_router = APIRouter(
    prefix="/titles",
    tags=["Titles"]
)

# Get All Titles
@title_router.get("/")
async def get_titles(db=Depends(get_db)):
    db_titles = db.query(TitleModel).all()# db_titles = conexión con db q lista (en formato BaseModel) *todos
    return db_titles

# Create Title
@title_router.post("/{title_id}", status_code=201, response_model=TitleResponse)
async def create_title(new_title: TitleRequest, db: Session = Depends(get_db)):
    db_title = TitleModel(**new_title.dict())
    db.add(db_title)
    db.commit()
    db.refresh(db_title)
    return db_title

# Get Title
@title_router.get("/{title_id}", status_code=201, response_model=TitleResponse)
async def get_title(title_id: int, db: Session = Depends(get_db)):
    db_title = db.query(TitleModel).filter(TitleModel.id == title_id).first()# db lista en formato BaseModel y filtra para q el id d la request es igual al id de la db) y devuelve el 1er resultado
    if not db_title:
        raise HTTPException(status_code=404, detail="User not found")
    return db_title

# Update Title
@title_router.put("/{title_id}", response_model=TitleResponse)
async def update_title(title_id: int, updated_title: TitleRequest, db=Depends(get_db)):
    db_title = db.query(TitleModel).filter(TitleModel.id == title_id).first()
    if not db_title:
        raise HTTPException(status_code=404, detail="Title not found")
    db_title.name = updated_title.name
    db_title.author = updated_title.author
    db_title.genre = updated_title.genre
    db_title.year = updated_title.year
    db.commit()
    db.refresh(db_title)
    return db_title

# Delete Title
@title_router.delete("/{title_id}")
async def delete_title(title_id: int, db=Depends(get_db)):
    db_title = db.query(TitleModel).filter(TitleModel.id == title_id).first()
    if not db_title:
        raise HTTPException(status_code=404, detail="Title not found")
    db.delete(db_title)
    db.commit()
    return {"message": "Title deleted successfully"}