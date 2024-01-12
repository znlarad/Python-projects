#Telegram basic bot answering to specific commands by user
#This code is written by znl_arad

import telegram
import telegram.ext
from telegram.ext import Updater
import os
import telebot

BOT_TOKEN=("------")# Telegram bot token is a private information because of that I didnt shared it 
#You should open your own bot and use the token from there

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['merhaba', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Merhabaaa ")
    
def handle_message(bot, update):
    chat_id = update.message.from_user.id
    text = 'Hello, World!'
    bot.send_message(chat_id=chat_id, text=text)


@bot.message_handler(commands=["no", "yes"])
def send_welcome(message):
    bot.reply_to(message, "Harika!!")
    

bot.infinity_polling()    
#Not allowing fot bot to stop

