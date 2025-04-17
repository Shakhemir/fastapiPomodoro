from fastapi import APIRouter, status

import fixtures
from schema.task import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/all", response_model=list[Task])
async def get_tasks():
    return fixtures.tasks


@router.post("/", response_model=Task)
async def create_task(task: Task):
    fixtures.tasks.append(task)
    return task


@router.patch("/{task_id}", response_model=Task)
async def patch_task(task_id: int, name: str):
    for task in fixtures.tasks:
        if task_id == task["id"]:
            task["name"] = name
            return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for idx, task in enumerate(fixtures.tasks):
        if task_id == task["id"]:
            del fixtures.tasks[idx]
            return {"message": "task deleted"}

    return {"message": "task not found"}
