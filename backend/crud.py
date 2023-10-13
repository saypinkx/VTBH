from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate


def get_user(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, password=user.password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
