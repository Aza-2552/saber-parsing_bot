from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
from keyboards import *
from seber_pars import pars_saber
from configs import get_value

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer('Salom!👋  Man SABER bot man! 📠')
    await show_category_saber(message)

async def show_category_saber(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Bolimni tanlang! 📑',
                           reply_markup=buttons_category())

@dp.message_handler(content_types=['text'])
async def get_shop_by_category(message: Message):
    chat_id = message.chat.id
    category_text = message.text
    get_product = pars_saber(get_value(category_text))

    for product in get_product:
        image = product.get('image')
        title = product.get('title')
        name_product = product.get('name_product')
        cost = product.get('cost')

        await message.answer_photo(photo=image, parse_mode='html', caption=f'''
<b>{title}</b>
{name_product}
<b>{cost}</b>''')

executor.start_polling(dp)

