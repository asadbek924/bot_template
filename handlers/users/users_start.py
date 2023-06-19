from aiogram.types import Message
from config  import dp
from aiogram.dispatcher import FSMContext
from keybords import home_kb
from filtrs import ISPRIVATE
@dp.message_handler(ISPRIVATE(),commands="start",state="*")
async def start(message:Message):
    await message.answer(f"Assalomu Alaykum {message.from_user.full_name}")

@dp.message_handler(text="clear")
async def clear(message:Message):
    await message.answer("tugmalar tozalandi")