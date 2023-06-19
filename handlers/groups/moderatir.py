from aiogram.types import Message
from config import dp
from filtrs import isgroup,AdminFilter
from datetime import datetime,timedelta
from aiogram.dispatcher.filters import Text
import asyncio
@dp.message_handler(isgroup(),AdminFilter(),Text(startswith="ban"))
async def spam_mode(message:Message):
    member=message.reply_to_message.from_user
    text=message.text.split(" ")
    check_time=text[1]
    check_result=text[2]
    if check_time.isdecimal():
        check_time=int(check_time)
        block_time=datetime.now()+timedelta(minutes=check_time)
        await message.chat.restrict(user_id=member.id,can_send_messages=False,until_date=block_time)
        await message.reply_to_message.delete()
        await message.delete()
        await message.answer(f"Foydalanuvchi {member.full_name} {check_time}  minutga {check_result} bloclandi")
        
@dp.message_handler(isgroup(),AdminFilter(),text="unban")
async def unban_mode(message:Message):
    member=message.reply_to_message.from_user
    await message.chat.restrict(user_id=member.id,can_send_messages=True,can_send_other_messages=True,can_send_media_messages=True)
    await message.answer(f" foydalanuvchi {member.full_name} blocklandi")
    await message.dalete()