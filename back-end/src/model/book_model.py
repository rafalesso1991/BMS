from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from datetime import datetime
# Book Model
class BookModel(Base):
    __tablename__ = 'books'

    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    owner_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)