from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, UTC


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    is_done:bool = False
    current_time: datetime = Field(default_factory=datetime.now(UTC))
    
    
class TaskResponse(BaseModel):
    id: int
    title:str
    is_done: bool
    current_time: datetime = Field(default_factory=datetime.now(UTC))