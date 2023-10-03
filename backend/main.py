import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from schemas import UserCreate
from database import SessionLocal
from models import User

from sqlalchemy.orm import Session
from database import Base,  engine
from config import ALGORITHM, SECRET_KEY
EXPIRATION_TIME = timedelta(hours=24)
oath2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base.metadata.create_all(bind=engine)


def create_jwt_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algoritm=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError:
        return None


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, password=user.password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_role(user: User) -> str:
    if user.is_entity:
        return "entity"
    elif user.is_superuser:
        return "admin"
    else:
        return "user"


def get_user(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/register")
def registered_user(user: UserCreate, db: Session = Depends(get_db)) -> UserCreate:
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    create_user(db, user)
    return user


@app.post("/token")
def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(db=db, username=username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    is_password_correct = pwd_context.verify(password, user.password)
    if not is_password_correct:
        raise HTTPException(status_code=400, detail="Incorrect password")
    jwt_token = create_jwt_token({"sub": (user.username, get_user_role(user))})
    return {"access_token": jwt_token, "token_type": "bearer"}

# def get_current_user(db: Session = Depends(get_db), token: str = Depends(oath2_scheme)):
#     decoded_data = verify_jwt_token(token)
#     if not decoded_data:
#         raise HTTPException(status_code=400, detail="Invalid token")
#     user = get_user(db=db, username=decoded_data['sub'])
#     if not user:
#         raise HTTPException(status_code=400, detail="User not found")
#     return user