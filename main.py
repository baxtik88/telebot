from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6485184019:AAG5W6bIzjDirpiTiBBZG2l8VFJIR1znzFo')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть web страницу',
                                    web_app=WebAppInfo(url='https://baxtik88.github.io/telebot/index.html')))
    await message.answer('Здравствуйте уважаемый посетитель!', reply_markup=markup)


executor.start_polling(dp)
