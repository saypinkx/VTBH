from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Boolean, Table, Column
from sqlalchemy.orm import mapped_column
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "User"
    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    email = mapped_column("email", String, nullable=True)
    username = mapped_column("username", String, nullable=False)
    password = mapped_column("password", String, nullable=False)
    registered_at = mapped_column("registered_at", TIMESTAMP, default=datetime.utcnow)
    is_superuser = mapped_column("is_superuser", Boolean, default=False)
    is_entity = mapped_column("is_entity", Boolean, default=False)
    is_active = mapped_column("is_active", Boolean, default=False)
