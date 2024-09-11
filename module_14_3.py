from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Информация'),
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Купить')
    ]
], resize_keyboard=True)

kb_remove = ReplyKeyboardRemove()

ib = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    ]
])


ib_price = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Витаминки 1', callback_data='product_buying'),
        InlineKeyboardButton(text='Витаминки 2', callback_data='product_buying'),
        InlineKeyboardButton(text='Витаминки 3', callback_data='product_buying'),
        InlineKeyboardButton(text='Витаминки 4', callback_data='product_buying')
    ]
])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(
        f'Привет, {message.from_user.username}! Я бот, помогающий твоему здоровью, чтобы узнать свою суточную норму калорий нажмите: Рассчитать',
        reply_markup=kb)


@dp.message_handler(text='Информация')
async def set_age(message):
    await message.answer(
        'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для оптимального похудения '
        'или сохранения нормального веса. Для того чтобы узнать вашу суточную норму калорий нажмите: Рассчитать',
        reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=ib)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Упрощенный вариант формулы Миффлина-Сан Жеора: '
                              '10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:', reply_markup=kb_remove)
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    w = float(data['weight'])
    g = float(data['growth'])
    a = float(data['age'])
    calories = 10.0 * w + 6.25 * g - 5.0 * a - 161.0
    await message.answer(f'Ваша суточная норма калорий: {calories}')
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('Files/1.jpg', 'rb') as img1:
        await message.answer_photo(img1, f'Название: Витаминки 1 | Описание: описание 1 | Цена: {1 * 100}')
    with open('Files/2.png', 'rb') as img2:
        await message.answer_photo(img2, f'Название: Витаминки 2 | Описание: описание 2 | Цена: {2 * 100}')
    with open('Files/3.jpg', 'rb') as img3:
        await message.answer_photo(img3, f'Название: Витаминки 3 | Описание: описание 3 | Цена: {3 * 100}')
    with open('Files/4.jpeg', 'rb') as img4:
        await message.answer_photo(img4, f'Название: Витаминки 4 | Описание: описание 4 | Цена: {4 * 100}')
    await message.answer('Выберите продукт для покупки', reply_markup=ib_price)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
