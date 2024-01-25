from fastapi import APIRouter, HTTPException
from .schema import UpdateTodoSchema, TodoSchema
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import cast, String
from .models import TodoModel
from ..dependencies import get_db, get_current_user
from uuid import uuid4


router = APIRouter(prefix="/todo")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_todo(db: Session = Depends(get_db), user=Depends(get_current_user)):
    todo_list = db.query(TodoModel).filter(TodoModel.userId == user).all()
    return {
        "success": True,
        "response": todo_list or [],
    }


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_todo(
    id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    todo = db.query(TodoModel).filter(TodoModel.todoId == id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo item not found"
        )

    return {
        "success": True,
        "response": todo,
    }


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(
    id: str, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    db.query(TodoModel).filter(TodoModel.todoId == id).delete(synchronize_session=False)
    db.commit()
    return {
        "success": True,
        "message": "Todo item deleted successfully",
    }


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def add_todo_item(
    req: TodoSchema, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    new_todo = TodoModel(
        todoId=cast(uuid4(), String),
        userId=user,
        title=req.title,
        description=req.description,
        isCompleted=False,
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return {
        "status": 201,
        "success": True,
        "message": "Todo item added successfully",
        "response": new_todo,
    }


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_todo(
    id: str,
    request: UpdateTodoSchema,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    todo = db.query(TodoModel).filter(TodoModel.todoId == id).first()

    if request.title is not None:
        todo.title = request.title
    if request.description is not None:
        todo.description = request.description
    if request.isCompleted is not None:
        todo.isCompleted = request.isCompleted

    db.commit()

    return {
        "status": 202,
        "success": True,
        "message": "Todo item updated successfully",
        "response": todo,
    }
