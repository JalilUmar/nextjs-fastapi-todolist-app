from fastapi import FastAPI
from .user.main import router as UserRouter
from .todo.main import router as TodoRouter
from .user import models as user_models
from .todo import models as todo_models
from .database import engine

app = FastAPI()


user_models.Base.metadata.create_all(bind=engine)
todo_models.Base.metadata.create_all(bind=engine)


@app.get("/hello")
def hello_world():
    return {"message": "Hello World"}


app.include_router(UserRouter)
app.include_router(TodoRouter)
