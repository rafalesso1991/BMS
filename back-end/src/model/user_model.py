from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime, Boolean
from datetime import datetime
# User Model
class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(255))
    email = Column(String(255))
    hashed_password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    logged_in = Column(Boolean, default=False)
    token = Column(String(255), default=None)