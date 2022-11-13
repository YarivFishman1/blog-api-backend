from fastapi import APIRouter, HTTPException, Depends
from src.models.comment import CommentUpdate
from sqlalchemy.orm import Session
from db.db import get_db
import db.crud.comment as crud


router = APIRouter(
    prefix="/comments",
    tags=["comment"],
    responses={404: {"description": "Not found"}},
)


@router.patch("/{comment_id}/")
async def update_post_comment(comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db)):
    if not crud.get_comment(db, comment_id):
        raise HTTPException(status_code=404, detail='Comment not found')
    crud.update_comment(db, comment_id, comment)
    return comment_id


@router.delete("/{comment_id}/")
async def delete_post_comment(comment_id: int, db: Session = Depends(get_db)):
    if not crud.get_comment(db, comment_id):
        raise HTTPException(status_code=404, detail='Comment not found')
    crud.delete_comment(db, comment_id)
    return comment_id
