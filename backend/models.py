from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Boolean, Table, Column
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "User"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String, nullable=True)
    username = Column("username", String, nullable=False)
    password = Column("password", String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    is_superuser = Column("is_superuser", Boolean, default=False)
    is_entity = Column("is_entity", Boolean, default=False)
    is_active = Column("is_active", Boolean, default=False)
