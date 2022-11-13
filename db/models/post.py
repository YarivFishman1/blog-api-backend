from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from db.db import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    body = Column(String(100))
    created_at = Column('createdAt', DateTime)
    blog_id = Column(Integer, ForeignKey('blogs.id'))

    blog = relationship('Blog', back_populates="posts")
    comments = relationship('Comment', back_populates='post')
