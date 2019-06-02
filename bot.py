import os
import telebot
from telebot.types import Message
TOKEN= 'add after'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='start')
def send_welcome(message):
    bot.reply_to(message,'Привет')

bot.polling()
