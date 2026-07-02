from pydantic import BaseModel, Field
from typing import Optional


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    is_done:bool = False
    
    
class TaskResponse(BaseModel):
    id:int
    title:str
    is_done: bool