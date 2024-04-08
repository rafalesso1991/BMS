from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, Boolean, DateTime
from datetime import datetime

# User Model
class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('title_id_seq'), primary_key=True)# 1
    username = Column(String(255))# 2
    email = Column(String(255))# 3
    admin = Column(Boolean, default=False)# 4
    hashed_password = Column(String(255))# 5
    created_at = Column(DateTime, default=datetime.utcnow)# 6
    updated_at = Column(DateTime, default=datetime.utcnow)# 7
