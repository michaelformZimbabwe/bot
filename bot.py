import telebot
from telebot import types
TOKEN= '698380037:AAG2JYt_oD7Cwbh2JtMEaavGQGb_yY-MPRw'
bot = telebot.TeleBot(TOKEN)
message = 'Привет мы любим Китай'

@bot.message_handler(commands='start')
def send_welcome(message):
    bot.reply_to(message)
