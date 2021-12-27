import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btcbutton = types.KeyboardButton("Новости")
    keyboard.add(btcbutton)
    return keyboard

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Привет, {name}!", reply_markup=get_keyboard())


@dp.message_handler(lambda message: message.text == "Новости")
async def getapi(message: types.Message):
    await message.reply("Сколько вывести новостей?")

@dp.message_handler()
async def default(message: types.Message):
    count = message.text
    ans = requests.get(f'http://172.17.0.2/home={count}')

    for i in ans.json():
         await message.answer(f"{i['caption']} {i['link']}")

    #await message.reply("Я работаю только с /news", reply_markup=get_keyboard())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
