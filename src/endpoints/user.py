from typing import List

from fastapi import APIRouter, HTTPException, Depends
from src.models.user import User, UserCreate, UserUpdate
from sqlalchemy.orm import Session
from db.db import get_db
import db.crud.user as crud

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[User])
async def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.post("/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db, user)


@router.patch("/{user_id}")
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    if not crud.get_user(db, user_id):
        raise HTTPException(status_code=404, detail='User not found')
    crud.update_user(db, user_id, user)
    return user_id


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not crud.get_user(db, user_id):
        raise HTTPException(status_code=404, detail='User not found')
    crud.delete_user(db, user_id)
    return user_id
