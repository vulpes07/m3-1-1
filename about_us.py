from aiogram import Router,types
from aiogram.filters import Command
router = Router()
@router.message(Command("о_нас"))
async def about_us_handler(message: types.Message):
    await message.answer("Мы — лучший бот! 🚀")