from database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from uuid import UUID


class TodoModel(Base):
    __tablename__ = "todo"

    todoId = Column(String, primary_key=True)
    userId = Column(String, ForeignKey("users.id"))
    title = Column(String)
    description = Column(String)
    isCompleted = Column(Boolean)
