from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from datetime import datetime
# Book Model
class BookModel(Base):
    __tablename__ = 'books'

    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    owner_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)