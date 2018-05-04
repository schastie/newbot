import os
import telebot
  
bot = telebot.TeleBot(os.environ['588205910:AAFYC9NrYLh3VH5DSdTIcu5u0Y9YxFRKbZY'])
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Hello, welcome to this bot!")
bot.polling()
