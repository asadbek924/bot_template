from aiogram import Dispatcher,Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
token="6239529760:AAE64bc0A9EK-pFZ-XoTb9NHw4tSEMTWIl0"
bot=Bot(token,parse_mode=ParseMode.HTML)
dp=Dispatcher(bot,storage=MemoryStorage())