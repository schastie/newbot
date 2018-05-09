# -*- coding: utf-8 -*-

import telebot
import sqlite3, csv

bot = telebot.TeleBot('588205910:AAFYC9NrYLh3VH5DSdTIcu5u0Y9YxFRKbZY')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    
     con = sqlite3.connect('edinput.db')
     cur = con.cursor()
     cur.execute("CREATE TABLE inp (inpId, inpEd);") # use your column names here

     with open('input.csv','rb') as fin: # `with` statement available in 2.5+
      # csv.DictReader uses first line in file for column headings by default
     dr = csv.DictReader(fin) # comma is default delimiter
     to_db = [(i['col1'], i['col2']) for i in dr]

     cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
     con.commit()
     con.close()
        
     bot.polling(none_stop=True)
