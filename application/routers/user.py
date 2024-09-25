from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from application.backend.db_depends import get_db
from typing import Annotated
from application.models import User
from application.shemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    else:
        return user


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create: CreateUser):
    db.execute(insert(User).values(username=create.username, firstname=create.firstname,
                                   lastname=create.lastname, age=create.age,
                                   slug=slugify(create.username)))
    db.commit()
    return {
        'statys_code': status.HTTP_201_CREATED,
        'translation': 'Successful'
    }


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], up_user: UpdateUser, user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(update(User).where(User.id == user_id).values(
        firstname=up_user.firstname,
        lastname=up_user.lastname,
        age=up_user.age))
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'User update is successful!'
    }


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'User delete is successful!'
    }