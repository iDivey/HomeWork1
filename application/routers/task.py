from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from application.backend.db_depends import get_db
from typing import Annotated
from application.models import Task, User
from application.shemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create: CreateTask, user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(insert(Task).values(title=create.title, content=create.content,
                                   priority=create.priority, user_id=user_id,
                                   slug=slugify(create.title)))
    db.commit()
    return {
        'statys_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, up_task: UpdateTask):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(update(Task).where(Task.id == task_id).values(
        title=up_task.title, content=up_task.content,
        priority=up_task.priority))

    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'User update is successful!'
    }


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'User update is successful!'
    }
