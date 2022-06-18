from bd_google import service, spreadsheetId , verify_data
from aiogram import executor
from loader import dp
import middlewares, handlers
from utils.notify_admins import on_startup_notify


data = verify_data()
print('Запуск бота')


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)