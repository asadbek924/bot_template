from aiogram.types import Message 
from config import dp 


@dp.message_handler(commands="start")
async def deeplink(message:Message):
    args=message.get_args()
    await message.answer(f"seni {args} taklif qiladi!")
@dp.message_handler(is_fowerded=True)
async def dep(message:Message):
    await message.answer(message)
