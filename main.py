from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6485184019:AAG5W6bIzjDirpiTiBBZG2l8VFJIR1znzFo')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть web страницу', web_app=WebAppInfo(url='https://itproger.com')))
    await message.answer('Здравствуйте уважаемы посетитель!', reply_markup=markup)


executor.start_polling(dp)
