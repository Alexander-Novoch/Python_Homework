from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config1 import TOKEN
# from tic_tac_toe import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

                                    # @dp.message_handler(commands=['start game'])
                                    # async def print_maps() -> win:
                                    #     return print("Победил" + win)
                                    # async def process_start_game_command(message: types.Message):
                                    #     await message.reply("Давай сыграем в крестики-нолики!")


if __name__ == '__main__':
    executor.start_polling(dp)


# import telebot
# from telebot import types
# from config1 import TOKEN
# bot=telebot.TeleBot(token=TOKEN)
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,'Привет')
# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1=types.KeyboardButton("Кнопка")
#     markup.add(item1)
#     bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text=="Кнопка":
#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1=types.KeyboardButton("Кнопка 2")
#         markup.add(item1)
#         bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
#     elif message.text=="Кнопка 2":
#         bot.send_message(message.chat.id,'Спасибо за прочтение статьи!')
# bot.infinity_polling()