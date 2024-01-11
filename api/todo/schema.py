from pydantic import BaseModel
from typing import Optional


class TodoSchema(BaseModel):
    title: str
    description: str


class UpdateTodoSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    isCompleted: Optional[bool] = None


class TodoResponseSchema(TodoSchema):
    todoId: str
    userId: str
    isCompleted: bool

    class Config:
        from_attributes = True
