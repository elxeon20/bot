from currency import Currency
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# import os

bot = Bot(token='5508872275:AAGRObICSLARPZsqpYy0IAMUeufp0cM1YaY', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_sender(message):
    #await message.answear(message.text)
    #await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)
    if list(message)[4][1] == 'b':
        a = Currency.get_info("UAH", "BUY", ['PrivatBank'])
        a = str(a)
        a = a.replace(',', '\n').replace('[','').replace(']','').replace("'","")
        return await message.reply(a)

    elif list(message)[4][1] == 's':
        a = Currency.get_info("UAH", "SELL", ['PrivatBank'])
        a = str(a)
        a = a.replace(',', '\n').replace('[','').replace(']','').replace("'","")
        return await message.reply(a)
    else:
        return await message.reply("Ввеведите 's' для поиска цены продаж \n Ввеведите 'b' для поиска цены покупок")


executor.start_polling(dp, skip_updates=True)
