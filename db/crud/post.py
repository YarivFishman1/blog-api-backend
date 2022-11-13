from sqlalchemy.orm import Session
from db.models.post import Post
from src.models.post import PostCreate, PostUpdate


def get_posts(db: Session, blog_id: int, skip: int = 0, limit: int = 100):
    return db.query(Post).filter(Post.blog_id == blog_id).offset(skip).limit(limit).all()


def get_post(db: Session, id: int):
    return db.query(Post).filter(Post.id == id).first()


def get_post_by_title(db: Session, title: str):
    return db.query(Post).filter(Post.title == title).first()


def create_post(db: Session, post: PostCreate):
    db_post = Post(title=post.title,
                   body=post.body,
                   created_at=post.created_at,
                   blog_id=post.blog_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post.id


def update_post(db: Session, id: int, post: PostUpdate):
    db.query(Post).filter(Post.id == id).update(post.dict())
    db.commit()


def delete_post(db: Session, id: int):
    db.query(Post).filter(Post.id == id).delete()
    db.commit()
