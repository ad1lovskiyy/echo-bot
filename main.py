from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, KeyboardButton

TOKEN = "6053961228:AAEEf-8sScZ5qB6xlaW6ElVOuUvLG-4k114"

bot = Bot(token=TOKEN)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
dp = Dispatcher(bot=bot)

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("❤️", callback_data="like"), InlineKeyboardButton("❌", callback_data="dislike")]
])

rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton(text="/help"))
rkb.add(KeyboardButton(text="/restart"))


# @dp.message_handler(commands=['start'])
# async def start_command(massage: types.Message):
#     await massage.reply(text="Qalaysan")


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


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSArj0DcwkAnsWv0rMYeFcWtletVFoTSZcGBM_4atU4yw&s",
                         caption="Bu rasm sizga yoqdimi?",
                         reply_markup=rkb)

@dp.callback_query_handler(text='like')
async def like_button(callback: types.CallbackQuery):
    await callback.answer("You like it")

@dp.callback_query_handler(text='dislike')
async def like_button(callback: types.CallbackQuery):
    await callback.answer("You dislike it")

if __name__ == '__main__':
    executor.start_polling(dp)