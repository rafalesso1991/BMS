from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime, Boolean
from datetime import datetime
# User Model
class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)# 1
    username = Column(String(255))# 2
    email = Column(String(255))# 3
    hashed_password = Column(String(255))# 4
    created_at = Column(DateTime, default=datetime.utcnow)# 6
    updated_at = Column(DateTime, default=datetime.utcnow)# 7
    logged_in = Column(Boolean, default=False)# 8
