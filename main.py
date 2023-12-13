import asyncio


from aiogram import Bot, Dispatcher,F
from aiogram import types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_pay,get_photo
from core.settings import settings
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



async def start_bot(bot : Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот Запущен' )

async def stop_bot(bot:Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


#start
async def start():
    bot = Bot(token=settings.bots.bot_token,parse_mode='HTML')
    dp = Dispatcher()
    
    dp.message.register(get_start,CommandStart())
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_pay, Command(commands=['pay']))
    dp.message.register(get_photo, F.photo)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()