from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    password = Column(String(15))
    full_name = Column('fullName', String(25))

    blogs = relationship('Blog', back_populates="user")
