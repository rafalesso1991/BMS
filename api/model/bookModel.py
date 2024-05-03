from config.db import Base
from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

# Book Model Table
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    owner = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
