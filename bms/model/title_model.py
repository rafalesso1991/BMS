from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from datetime import datetime

class TitleModel(Base):
    __tablename__ = 'titles'

    id = Column(Integer, Sequence('title_id_seq'), primary_key=True)
    name = Column(String(255))
    author = Column(String(255))
    genre = Column(String(255))
    year = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
