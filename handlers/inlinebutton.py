from aiogram.types import Message,CallbackQuery
from config import dp
from keybords import test_in_kb,raqam_kb
from random import randint


@dp.message_handler(commands="start")
async def start(message:Message):
    await message.answer("Ushbu xabar osti tugmasi siz uchun",reply_markup=test_in_kb)


@dp.callback_query_handler(text="Asadbek")
async def callback(call:CallbackQuery):
    # # await call.answer("Sen test bo'limidasan",show_alert=True)
    # name=call.message.chat.first_name
    # await call.message.answer(f"{name} Sen test line tugmasi bosdingiz")
    data=call.data
    await call.answer(data,show_alert=True)


@dp.callback_query_handler(text="random")
async def rand(call:CallbackQuery):
    tasodif=randint(0,1000)
    await call.message.answer(f"tasodifiy son {tasodif}")
@dp.message_handler(commands="kara")
async def kara(message:Message):
    await message.answer("Kerakli raqmni bosing",reply_markup=raqam_kb())
@dp.callback_query_handler(text_startswith="raqam")

async def karakara(call:CallbackQuery):
    data=call.data
    son=int(data.split("_")[1])
    info=""
    for i in range(1,11):
        info+=f"{son}*{i}={son*i}\n"
    await call.message.reply(info)
    
