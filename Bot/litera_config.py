from aiogram.dispatcher.filters.state import State, StatesGroup
API = '7480257389:AAEGJTm77ViFzdpNbZlnAE9VB_KZM0Vmzn0'


class BookState(StatesGroup):
    author = State()
    name_father_Author = State()
    title = State()
    publisher = State()
    city = State()
    year = State()
    pages = State()
