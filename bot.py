from aiogram import Dispatcher, Bot, types, executor
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
from config import *
from datetime import datetime

from weather import Weather

API_TOKEN = "2139720619:AAHsA5Y0RUSJXfKJDB_xQ7UF6USh-bCQzbQ"
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(
        "Hello, it's a bot, which can send you <b>latest news</b>, <b>weather broadcats</b> and <b>exchange rates</b>!",
        parse_mode=types.ParseMode.HTML)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Weather Broadcasts", "Latest News", "Exchange Rates"]
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
    URL = 'https://www.unian.ua/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.findAll('a', 'list-news__title')

    for i in range(0, len(texts[:-20])):
        txt = str(i + 1) + ') ' + texts[i].text
        await bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode='html')


@dp.message_handler(lambda message: message.text == "Exchange Rates")
async def exchange_rates(message: types.Message):
    await message.answer("Exchange Rates was chosen")


if __name__ == "__main__":
    executor.start_polling(dp)
