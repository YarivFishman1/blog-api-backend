from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.db import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='blogs')
