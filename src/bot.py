from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import cred
import binance_functions

bot = Bot(token=cred.telegram_token)
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text=" BTCUSDT ", callback_data="BTCUSDT")
button2 = InlineKeyboardButton(text=" RAYUSDT", callback_data="RAYUSDT")
button3 = InlineKeyboardButton(text=" DUSKUSDT", callback_data="DUSKUSDT")
button4 = InlineKeyboardButton(text=" SKLUSDT", callback_data="SKLUSDT")
button5 = InlineKeyboardButton(text=" Cancel", callback_data="cancel")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("🪙 Select Symbols", "📑 Support")


@dp.message_handler(commands=['start'])
async def symbol_selection(message: types.Message):
    await message.reply("Select the Symbol", reply_markup=(keyboard_inline))


@dp.message_handler(commands=['help'])
async def welcome(message: types.Message):
    await message.reply("Cancelled ", reply_markup=keyboard1)


@dp.callback_query_handler(text=["cancel", "BTCUSDT", "RAYUSDT", "DUSKUSDT", "SKLUSDT"])
async def random_value(call: types.CallbackQuery):
    if call.data == "BTCUSDT":
        res = binance_functions.get_historical_klines(call.data)
        await call.message.answer(f"The price changed percentage of {call.data} over the past week is {res[1]}%",
                                  reply_markup=keyboard1)
        await call.message.reply_photo(res[0], reply_markup=keyboard1)

    if call.data == "RAYUSDT":
        res = binance_functions.get_historical_klines(call.data)
        await call.message.answer(f"The price changed percentage of {call.data} over the past week is {res[1]}%",
                                  reply_markup=keyboard1)
        await call.message.reply_photo(res[0], reply_markup=keyboard1)
    if call.data == "DUSKUSDT":
        res = binance_functions.get_historical_klines(call.data)
        await call.message.answer(f"The changed percentage of {call.data} over the past week is {res[1]}%",
                                  reply_markup=keyboard1)
        await call.message.reply_photo(res[0], reply_markup=keyboard1)
    if call.data == "SKLUSDT":
        res = binance_functions.get_historical_klines(call.data)
        await call.message.answer(f"The price changed percentage of {call.data} over the past week is {res[1]}%",
                                  reply_markup=keyboard1)
        await call.message.reply_photo(res[0], reply_markup=keyboard1)
    if call.data == "cancel":
        await call.message.answer("Cancelled", reply_markup=keyboard1)
    await call.answer()


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '🪙 Select Symbols':
        await message.reply("Select the Symbol", reply_markup=(keyboard_inline))
    elif message.text == '📑 Support':
        await message.reply("Please refer the following link to learn about Binance API! "
                            "https://www.binance.com/en/binance-api ", reply_markup=keyboard1)
    else:
        await message.reply(f"Your message is: {message.text}. One of our agent will reply to that soon.")


executor.start_polling(dp)
