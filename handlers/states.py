from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext
@dp.message_handler(commands="register")
async def register(message:Message,state:FSMContext):
    await message.answer("Famila ismingni kirit>>>F.I.SH")
    await state.set("register")
@dp.message_handler(state="register")  
async def fullname(message:Message,state:FSMContext):
    ism=message.text
    await message.answer(f"{ism} telefon raqam kirit:")
    await state.set_state("phone")
@dp.message_handler(state="phone")
async def phone(message:Message,state:FSMContext):
    tel=message.text
    await message.answer(f"seni telifoning {tel}")
    await state.finish()