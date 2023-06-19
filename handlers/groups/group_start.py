
from aiogram.types import Message
from config  import dp
from aiogram.dispatcher import FSMContext

from filtrs import isgroup,AdminFilter

@dp.message_handler(isgroup(),commands="start",state="*")
async def start(message:Message):
    await message.answer(f"Assalomu Alaykum {message.from_user.full_name} Siz grouppaga xush kelibsiz!!!")






