from aiogram import Router,types
from bot import bot
from aiogram.filters import Command
from reply import menu_keyboard
router = Router()
@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')
    await message.answer("Главное меню:", reply_markup=menu_keyboard)