from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    email: str
    password: str
    full_name: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str


class UserUpdate(BaseModel):
    password: Optional[str] = None
    full_name: Optional[str] = None
