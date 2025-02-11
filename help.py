from aiogram import Router,types
from aiogram.filters import Command
router = Router()
@router.message(Command("помощь"))
async def help_handler(message: types.Message):
    await message.answer( "Напишите нам, если у вас есть вопросы! 💬")