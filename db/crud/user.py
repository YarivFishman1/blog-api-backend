from sqlalchemy.orm import Session
from db.models.user import User
from src.models.user import UserCreate, UserUpdate


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password=user.password, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.id


def update_user(db: Session, id: int, user: UserUpdate):
    db.query(User).filter(User.id == id).update(user.dict())
    db.commit()


def delete_user(db: Session, id: int):
    db.query(User).filter(User.id == id).delete()
    db.commit()
