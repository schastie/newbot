# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot('588205910:AAFYC9NrYLh3VH5DSdTIcu5u0Y9YxFRKbZY')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
