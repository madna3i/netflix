from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Team", reply_markup=menu)

@dp.message_handler(Text(equals=["Drama","Horror", "Serials","Comedy"]))
async def get_food(message: Message):
    await message.answer(f" {message.text}. Chosen", reply_markup=ReplyKeyboardRemove())