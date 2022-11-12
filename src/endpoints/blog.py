from fastapi import APIRouter, HTTPException, Depends
from src.models.blog import BlogCreate, BlogUpdate
from sqlalchemy.orm import Session
from db.db import get_db
import db.crud.blog as crud
import db.crud.post as post_crud


router = APIRouter(
    prefix="/blogs",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{blog_id}/")
async def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return crud.get_blog(db, blog_id)


@router.post("/")
async def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db, blog)


@router.patch("/{blog_id}/")
async def update_blog(blog_id: int, blog: BlogUpdate, db: Session = Depends(get_db)):
    if not crud.get_user(db, blog_id):
        raise HTTPException(status_code=404, detail='Blog not found')
    crud.update_user(db, blog_id, blog)
    return blog_id


@router.delete("/{blog_id}/")
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    if not crud.get_user(db, blog_id):
        raise HTTPException(status_code=404, detail='Blog not found')
    crud.delete_user(db, blog_id)
    return blog_id


@router.get("/{blog_id}/posts")
async def get_posts(blog_id: int, db: Session = Depends(get_db)):
    post_crud.get_posts(db, blog_id)
