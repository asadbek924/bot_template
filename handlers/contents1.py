from aiogram.types import Message,ContentTypes
from config import dp
@dp.message_handler(content_types="text")
async def texts(message:Message):
    await message.answer(f"{message.from_user.full_name} sen {message.text} xabarlarni stickerini jo'nat")
@dp.message_handler(content_types="sticker")
async def sticker(message:Message):
    await message.reply(f"seni stickering emojisi {message.sticker.emoji}")
    await message.answer_sticker()
@dp.message_handler(content_types=ContentTypes().CONTACT)
async def rasmlara(message:Message):
    await message.answer("sen contact yubording")