from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
dp = Dispatcher()
class MyStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()

@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(MyStates.waiting_for_name)

@dp.message(MyStates.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Yoshingizni kiriting:")
    await state.set_state(MyStates.waiting_for_age)

@dp.message(MyStates.waiting_for_age)
async def get_age(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f"Salom, {user_data['name']}! Yoshingiz {message.text}.")
    await state.clear()
