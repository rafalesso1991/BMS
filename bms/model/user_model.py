from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, Boolean, DateTime
from datetime import datetime

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('title_id_seq'), primary_key=True)
    username = Column(String(255))
    email = Column(String(255))
    admin = Column(Boolean, default=False)
    hashed_password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
