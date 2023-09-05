from typing import Any
from fastapi import FastAPI, Depends, HTTPException, status

blogs = {
    "1": "FastAPI Prerequesites",
    "2": "Building APIs with FastAPI",
    "3": "Background Tasks | Celery x FastAPI",
}

users = {"1": "Jamie", "2": "Romie"}

app = FastAPI(title="Dependency Injection")


def get_blog_or_404(model: dict, id: str):
    obj = model.get(id)
    if not obj:
        raise HTTPException(
            detail=f"Blog with id: {id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return obj


class GetObjectOr404:
    def __init__(self, model) -> None:
        self.model = model

    def __call__(self, id: str) -> Any:
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(
                detail=f"Object with id: {id} does not exist",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return obj


@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(get_blog_or_404)):
    return blog_name

user_dependancy = GetObjectOr404(users)
@app.get("/user/{id}")
def get_user(user_name:str = Depends(user_dependancy)):
    return user_name