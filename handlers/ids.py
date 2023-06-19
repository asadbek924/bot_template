from aiogram.types import Message
from config import dp
@dp.message_handler(chat_id=5421427581,text="admin")
async def admin(message:Message):
    await message.reply("salom admin")