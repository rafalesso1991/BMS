from config.db import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

class BookModel(Base):
    __tablename__ = 'books'

    title_id = Column(Integer, ForeignKey('titles.id'), primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    #quantity = Column(Interger)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
