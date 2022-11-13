from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        orm_mode = True


class BlogCreate(BaseModel):
    name: str
    user_id: int


class BlogUpdate(BaseModel):
    name: Optional[str] = None
