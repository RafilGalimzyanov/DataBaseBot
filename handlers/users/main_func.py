from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data
from aiogram.utils.markdown import hlink

from handlers.users.parsing import dollar
from loader import dp, bot
from states.trip import Trip
from bd_postgreSQL import filling_bd
from bd_google import verify_data

@dp.callback_query_handler(text="data", state=None)
async def go_ord(query: types.CallbackQuery):
    doll = dollar()
    '''
    PostgreSQL не заполняю, при необходимости просто уберу коммент функции filling_bd
    '''
    filling_bd()
    user_id = query.message.chat.id
    await bot.delete_message(user_id, query.message.message_id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Обновить", callback_data="data", messages="one"))
    text = verify_data()

    for i in text:
        try:
            i.insert(3, float('{:.3f}'.format(float(i[2]) * doll)))
        except:
            pass
    res = ",\n".join(map(str, text))

    await bot.send_message(chat_id=user_id,text=f"Number, Order_ID, Price_$, Price_rub, Timing:\n"
                                                f"{res}", reply_markup=keyboard)
