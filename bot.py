import telebot
from telebot import apihelper
TOKEN= '698380037:AAG2JYt_oD7Cwbh2JtMEaavGQGb_yY-MPRw'
apihelper.proxy = {'https: socks4://198.50.214.17:6874'}
bot = telebot.TeleBot(TOKEN)
message = 'Привет мы любим Китай'

@bot.message_handler(commands='start')
def send_welcome(message):
    bot.send_message(message)
