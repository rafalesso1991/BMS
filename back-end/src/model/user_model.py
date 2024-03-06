from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from datetime import datetime
# User Model
class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)