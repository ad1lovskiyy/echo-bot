from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "6053961228:AAGDFZGrZY0r-7FLWjtZ0ZxRIEcbY7l9ZyM"

bot = Bot(token=TOKEN)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(massage: types.Message):
    await massage.reply(text="Qalaysan")


"""@dp.message_handler()
async def echo_ansver(massage: types.Message):
    await massage.answer(text=massage.text.upper())"""


@dp.message_handler(Text(equals="commands"))
async def get_commands(massage: types.Message):
    text = """
        /newbot - start bot
        /mybots - help command
    """
    await massage.answer(text=text)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
