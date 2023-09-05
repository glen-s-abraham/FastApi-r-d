from pydantic import BaseModel, Field
from typing import Optional,List
from enum import Enum
from datetime import datetime


class Language(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

class Comment(BaseModel):
    text:Optional[str] = None

class Blog(BaseModel):
    title: str = Field(min_length=10)
    description: Optional[str] = None
    is_active: bool
    language: Language = Language.JAVA
    created_at: datetime = Field(default_factory=datetime.now)
    comments:Optional[List[Comment]]


first_blog = Blog(title="My title for the blog 1", is_active=True,comments=[{'text':'kool'}])
print(first_blog)


