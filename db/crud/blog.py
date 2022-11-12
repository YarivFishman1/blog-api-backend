from sqlalchemy.orm import Session
from db.models.blog import Blog
from src.models.blog import BlogCreate, BlogUpdate


def get_blogs(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Blog).filter(Blog.user_id == user_id).offset(skip).limit(limit).all()


def get_blog(db: Session, id: int):
    return db.query(Blog).filter(Blog.id == id).first()


def get_blog_by_name(db: Session, name: str):
    return db.query(Blog).filter(Blog.name == name).first()


def create_blog(db: Session, blog: BlogCreate):
    db_blog = Blog(name=blog.name, user_id=blog.user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog.id


def update_blog(db: Session, id: int, blog: BlogUpdate):
    db.query(Blog).filter(Blog.id == id).update(blog.dict())
    db.commit()


def delete_blog(db: Session, id: int):
    db.query(Blog).filter(Blog.id == id).delete()
    db.commit()
