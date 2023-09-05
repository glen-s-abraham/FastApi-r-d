import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings:
    PROJECT_TITLE: str = "Blog"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.environ.get("POSTGRES_SERVER")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
