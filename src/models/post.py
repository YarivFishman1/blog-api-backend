from datetime import date
from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    id: int
    title: str
    body: str
    created_at: date
    blog_id: str

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    body: str
    blog_id: str


class PostUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
