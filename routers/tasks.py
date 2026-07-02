from fastapi import APIRouter, HTTPException, status
from app.schemas import TaskCreate, TaskResponse


router = APIRouter(prefix="/tasks", tags=["tasks"])

#In-memory storage for tasks
fake_db: dict[int, dict] = {}
next_id = 1



@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id
    record = {"id": next_id, **task.model_dump()}
    fake_db[next_id] = record
    next_id += 1
    return record


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return fake_db[task_id]


@router.get("/", response_model=list[TaskResponse])
def list_tasks(is_done:bool | None = None, limit: int =10):
    results =list(fake_db.values())
    if is_done is not None:
        results = [t for t in results if t["is_done"] == is_done]
    return results[:limit]    