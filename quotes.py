import telebot
from bs4 import BeautifulSoup
import requests
import re
from telebot import types

token = "" #token @BotFather

########################### Bot #########################
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
  site = "https://citaty.info/random"
  html_text = requests.get(site).text
  soup = BeautifulSoup(html_text, 'lxml')
  citata = soup.find('div', class_='field-item even last').text
  bot.send_message(message.chat.id, citata)

bot.polling(none_stop=True)
