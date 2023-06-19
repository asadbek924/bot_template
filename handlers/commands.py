from aiogram import types
from config import dp
from aiogram.dispatcher.filters.builtin import Command
@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer(f"salom {message.chat.full_name}")
@dp.message_handler(commands="salom")
async def hello(message:types.Message):
    await message.reply(f"sen {message.text} buyruqni ishlatding??!")
@dp.message_handler(Command=("kun"))
async def kun(message:types.Message):
    await message.reply(f"bugun havo issiq")

