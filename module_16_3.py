from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def home() -> str:
    return "Главная страница"


@app.get("/users")
def all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
def new_user(username: Annotated[str, Path(max_length=20, min_length=2, description='Введите имя пользователя', example='Вася')],
             age:  Annotated[int, Path(ge=15, le=120, description='Введите ваш возраст', example='20')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[str, Path(max_length=4, min_length=1, description='Введите id пользователя', example='1')],
                username: Annotated[str, Path(max_length=20, min_length=2, description='Введите имя пользователя', example='Вася')],
                age:  Annotated[int, Path(ge=15, le=120, description='Введите ваш возраст', example='20')]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[str, Path(max_length=4, min_length=1, description='Введите id пользователя', example='1')]):
    users.pop(user_id)
    return f"User {user_id} has been deleted"
