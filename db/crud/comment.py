from sqlalchemy.orm import Session
from db.models.post import Comment
from src.models.comment import CommentCreate, CommentUpdate


def get_comments(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.query(Comment).filter(Comment.post_id == post_id).offset(skip).limit(limit).all()


def get_comment(db: Session, id: int):
    return db.query(Comment).filter(Comment.id == id).first()


def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(title=comment.title,
                         created_at=comment.created_at,
                         post_id=comment.post_id,
                         user_id=comment.user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment.id


def update_comment(db: Session, id: int, comment: CommentUpdate):
    db.query(Comment).filter(Comment.id == id).update(comment.dict())
    db.commit()


def delete_comment(db: Session, id: int):
    db.query(Comment).filter(Comment.id == id).delete()
    db.commit()
