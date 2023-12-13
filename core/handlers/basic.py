from aiogram import Bot
from aiogram import types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher
from aiogram import types



#Обработка кнопки start
async def get_start(message:Message,bot:Bot):
    await bot.send_message(message.from_user.id,f'<b>Привет {message.from_user.first_name}.Рад тебя видеть</b>')


async def get_pay(message: Message,bot:Bot):

    #Кнопка оплатил
#    buttons_keyboard = InlineKeyboardMarkup()
#   button_pay = InlineKeyboardButton(text='оплатил', callback_data='paid')  # Добавлен параметр callback_data для обработки нажатия на кнопку
#    buttons_keyboard.add(button_pay)
    await bot.send_message(message.from_user.id,f'Реквезиты для оплаты.После оплаты, нажмите - ОПЛАТИЛ, и после этого приложите чек')#, reply_markup=buttons_keyboard)
    

async def get_photo(message:Message,bot:Bot):
    await message.answer(f'Отлично. Обрабатываю заявку')


