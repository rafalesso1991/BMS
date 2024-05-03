from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, Boolean
from sqlalchemy.orm import relationship

# User Model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255))
    active = Column(Boolean, default=False)
    books = relationship('Book', backref='user')
