from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_orm import BaseORM

# def create_tables():
#     BaseORM.metadata.create_all(bind=engine)


def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    return app


app = start_app()


@app.get("/")
def index():
    return {"msg": "hello FastAPI"}
