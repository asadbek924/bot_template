from aiogram.types import Message
from config import dp
@dp.message_handler(hashtag="money")
async def tag(message:Message):
    await message.reply("akang kuchaydi")
