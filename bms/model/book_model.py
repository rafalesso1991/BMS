from config.db import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

# Book Model
class BookModel(Base): #FALTA HEREDAR
    __tablename__ = 'books'

    title_id = Column(Integer, ForeignKey('titles.id'), primary_key=True)# 1
    owner_id = Column(Integer, ForeignKey('users.id'), primary_key=True)# 2
    created_at = Column(DateTime, default=datetime.utcnow)# 3
    updated_at = Column(DateTime, default=datetime.utcnow)# 4
 