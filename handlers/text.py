from aiogram.types import Message
from config import dp
from aiogram.dispatcher.filters import Text
@dp.message_handler(text="telefon")
async def phone(message:Message):
    await message.answer("seni telefoning qanaqa?")
@dp.message_handler(text="/yordam")
async def helpme(message:Message):
    await message.reply("vooooy yoooordammmm")
@dp.message_handler(Text("kimsan"))
async def kimsan(message:Message):
    await message.reply("men Tursinxonman")
@dp.message_handler(Text(startswith="ali"))
async def ali(message:Message):
    await message.reply("sen jon so'zi bilan tugallangan text yubording")
@dp.message_handler(Text(contains="ahmoq"))
async def ahmoq(message:Message):
    await message.reply("sen taqiqlangan so'zi bilan boshlangan text yubording")
@dp.message_handler(text_contains="ona")
async def ona(message:Message):
    await message.reply("ona buyuk zot")
@dp.message_handler(text="info")
async def nomalum(message:Message):
    await message.reply(message)