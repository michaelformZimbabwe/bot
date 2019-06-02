import os
import telebot
from telebot.types import Message
TOKEN= '698380037:AAG2JYt_oD7Cwbh2JtMEaavGQGb_yY-MPRw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='start')
def send_welcome(message):
    bot.send_message(message,'Привет')
