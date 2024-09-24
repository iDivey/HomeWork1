from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()


users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def home() -> str:
    return "Главная страница"


@app.get("/users")
def all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def new_user(user: User, username: Annotated[str, Path(max_length=20, min_length=2, description='Введите имя пользователя', example='Вася')],
             age: Annotated[int, Path(ge=15, le=120, description='Введите ваш возраст', example='20')]) -> str:
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return f"Пользователь {user} is registered"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int, Path(ge=1, le=1000, description='Введите id пользователя', example='1')],
                username: Annotated[str, Path(max_length=20, min_length=2, description='Введите имя пользователя', example='Вася')],
                age:  Annotated[int, Path(ge=15, le=120, description='Введите ваш возраст', example='20')]) -> User:
    try:
        update_u = users[user_id]
        update_u.age = age
        update_u.username = username
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(ge=1, le=1000, description='Введите id пользователя', example='1')]):
    try:
        users.pop(user_id)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
