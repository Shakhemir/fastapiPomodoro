from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.post("/task/{task_id}")
async def post_task(task_id: int):
    return {"task": task_id}


@router.get("/tasks")
async def get_tasks():
    return []

