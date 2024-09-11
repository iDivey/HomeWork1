from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
kb.add(button1)
kb.add(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью, чтобы узнать свою суточную норму калорий нажмите: Рассчитать',
        reply_markup=kb)


@dp.message_handler(text='Информация')
async def set_age(message):
    await message.answer(
        'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для оптимального похудения '
        'или сохранения нормального веса. Для того чтобы узнать вашу суточную норму калорий нажмите: Рассчитать',
        reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


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


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
