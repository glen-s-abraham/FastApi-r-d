from fastapi import FastAPI

from server.routes.student import router  as StudentRouter
from server.routes.user import router  as UserRouter


app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(UserRouter, tags=["User"], prefix="/user")


