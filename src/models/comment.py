from datetime import date

from pydantic import BaseModel
from typing import Optional


class Comment(BaseModel):
    comment_id: int
    body: str
    created_at: date
    post_id: int
    user_id: str

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    post_id: int
    user_id: str
    title: str
    body: str


class CommentUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
