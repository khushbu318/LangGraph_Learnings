from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Todo:
    id: int
    title: str
    desc: str
    is_comp: bool
    priority: int
    created_at: datetime

    def __init__(self,id, title, desc, is_comp, priority):
        self.id = id
        self.title = title
        self.desc = desc
        self.is_comp = is_comp
        self.priority = priority
        self.created_at = datetime.now()


class TodoRequest(BaseModel):
    id: Optional[int] = Field(ge=1, default=None)
    title: str = Field(min_length=2, max_length=50)
    desc: str
    is_completed: Optional[bool] = Field(default=False)
    priority: int =  Field(le=5, ge=1)

