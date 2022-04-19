#keyboard.defalt
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Drama"),
            KeyboardButton(text="Horror")
        ],
        [
            KeyboardButton(text="Serials"),
            KeyboardButton(text="Comedy")
        ],
    ],
    resize_keyboard=True
)