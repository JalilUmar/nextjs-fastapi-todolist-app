from fastapi import FastAPI
from user.main import router as UserRouter
from todo.main import router as TodoRouter
import user.models as user_models
import todo.models as todo_models
from database import engine

app = FastAPI()


user_models.Base.metadata.create_all(bind=engine)
todo_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


app.include_router(UserRouter)
app.include_router(TodoRouter)
