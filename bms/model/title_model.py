from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from datetime import datetime

# Title Model
class TitleModel(Base):
    __tablename__ = 'titles'

    id = Column(Integer, Sequence('title_id_seq'), primary_key=True)# 1
    name = Column(String(255))# 2
    author = Column(String(255))# 3
    genre = Column(String(255))# 4
    year = Column(Integer)# 5
    created_at = Column(DateTime, default=datetime.utcnow)# 6
    updated_at = Column(DateTime, default=datetime.utcnow)# 7
