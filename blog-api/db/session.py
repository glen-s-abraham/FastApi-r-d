from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

print(settings.DATABASE_URL)

engine = create_engine(settings.DATABASE_URL)

SESSION_LOCAL = sessionmaker(autoflush=False,autocommit=False,bind=engine)