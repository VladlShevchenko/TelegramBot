from aiogram import Dispatcher, Bot, types, executor
import requests 
import json
from config import *
from datetime import datetime
API_TOKEN = "2139720619:AAHsA5Y0RUSJXfKJDB_xQ7UF6USh-bCQzbQ"
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("Hello, it's a bot, which can send you <b>latest news</b>, <b>weather broadcats</b> and <b>exchange rates</b>!", parse_mode=types.ParseMode.HTML)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Weather Broadcasts","Latest News", "Exchange Rates"]
    keyboard.add(*buttons)
    await message.answer("What you want to choose?", reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def help_handler(): 
    """
    help handler
    """
    pass



@dp.message_handler(lambda message: message.text == "Weather Broadcasts")
async def weather_news(message: types.Message):
    await message.answer("Weather Broadcast was chosen")

@dp.message_handler(lambda message: message.text == "Latest News")
async def latest_news(message: types.Message):
    await message.answer("Latest News was chosen")

@dp.message_handler(lambda message: message.text == "Exchange Rates")
async def exchange_rates(message: types.Message):
    await message.answer("Exchange Rates was chosen")

if __name__ == "__main__":
    executor.start_polling(dp)
