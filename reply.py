from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/о_нас"),KeyboardButton(text="/помощь")]
    ],
    resize_keyboard=True
)
__all__ = ["menu_keyboard"]  