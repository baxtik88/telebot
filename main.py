from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
bot = Bot('6485184019:AAG5W6bIzjDirpiTiBBZG2l8VFJIR1znzFo')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть web страницу',
                                    web_app=WebAppInfo(url='https://baxtik88.github.io/telebot/index.html')))
    await message.answer('Здравствуйте уважаемый посетитель!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name : {res["name"]} ;\n Emale : {res["email"]} ;\n Phone : {res["phone"]}')


executor.start_polling(dp)
