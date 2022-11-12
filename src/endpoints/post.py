from fastapi import APIRouter, HTTPException, Depends
from src.models.post import PostCreate, PostUpdate
from src.models.comment import CommentCreate
from sqlalchemy.orm import Session
from db.db import get_db
import db.crud.post as crud


router = APIRouter(
    prefix="/posts",
    tags=["post"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def get_posts(db: Session = Depends(get_db)):
    return crud.get_posts()


@router.get("/{post_id}/")
async def get_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post(db, post_id)


@router.post("/")
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)


@router.patch("/{post_id}/")
async def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    if not crud.get_user(db, post_id):
        raise HTTPException(status_code=404, detail='User not found')
    crud.update_user(db, post_id, post)
    return post_id


@router.delete("/{post_id}/")
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    if not crud.get_user(db, post_id):
        raise HTTPException(status_code=404, detail='User not found')
    crud.delete_user(db, post_id)
    return post_id


@router.get("/{post_id}/comments/")
async def get_post_comments(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post_comments(db, post_id)


@router.post("/{post_id}/comments/")
async def add_post_comment(post_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    return crud.add_post_comment(db, post_id, comment)
