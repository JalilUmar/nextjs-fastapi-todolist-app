from database import Base
from sqlalchemy import Column, String
from uuid import UUID


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=UUID)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
