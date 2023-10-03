from pydantic import BaseModel
class UserCreate(BaseModel):
    email: str
    username: str
    password: str

    class Config:
        orm_mode = True