# -*- coding: utf-8 -*-

import telebot
import sqlite3, csv

bot = telebot.TeleBot('588205910:AAFYC9NrYLh3VH5DSdTIcu5u0Y9YxFRKbZY')
mestext = 'hello';
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    
     con = sqlite3.connect('input.sqlite')
     cur.execute("select x from Table limit 1")
     for row in cur:
        mestext = row;
     con.close()
        
     bot.polling(none_stop=True)
