from config.db import Base
from sqlalchemy import Column, Integer, Sequence, DateTime
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


""" # Book Model
class BookModel(Base): #FALTA HEREDAR
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title_id = Column(Integer, ForeignKey('titles.id'), nullable=False)   
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)#
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
 """