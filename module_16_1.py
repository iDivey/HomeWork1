from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def users(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user(username: str = 'user', age: int = 100) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"