from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_orm import BaseORM


class User(BaseORM):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog",back_populates='author')