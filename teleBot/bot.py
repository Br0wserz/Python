#!/usr/bin/python

import telegram

#bot = telegram.Bot(token="308937285:AAGki0QsC0JmWMFFX7hDq_ZI0UTiKALOsKo")
bot = telegram.Bot(token="296505578:AAHV-r5TOb2s_HO_ggs4DdYlGttUnIAeW08")
updates=[]
while not updates:
     updates = bot.getUpdates()[-1]
     id = updates.message.chat_id
#print updates[-1].message.text
#chat_id = 124490713
#msg = raw_input("Mandami un messaggio: ")
#bot.sendMessage(chat_id = 210632508, text= "we")

print id
