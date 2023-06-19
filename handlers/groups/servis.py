from aiogram.types import Message,ContentType
from config import dp
from filtrs import isgroup,AdminFilter
@dp.message_handler(isgroup(),content_types=ContentType.NEW_CHAT_MEMBERS)
async def new_member(message:Message):
    members=message.new_chat_members     
    for member in members:
        await message.reply(f"guruhga xush kelibsiz!!!  \n {member.get_mention(as_html=True)}")
@dp.message_handler(isgroup(),content_types=ContentType.LEFT_CHAT_MEMBER)
async def left_member(message:Message):
    await message.dalete()
    member=message.left_chat_member
    if member.id==message.from_user.id:
        await message.answer(f"{member.get_mention(as_html=True)} guruhni tark etdi")
    else:
        await message.answer(f"{member.full_name} guruhdan haydaldi")