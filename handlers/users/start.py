from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from bd_google import our_table

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    driver_id = message.from_user.id
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Посмотреть базу поставок", callback_data="data", messages="one"))
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Этот тестовый Бот предназначен для контроля базы поставок\n"
                         f"Ссылка на таблицу для правки: {our_table}", reply_markup=keyboard)