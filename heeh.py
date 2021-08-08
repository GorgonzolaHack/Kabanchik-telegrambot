# -*- coding: utf8 -*-
#1030811973
import telebot
import requests
from fake_useragent import UserAgent
from time import sleep
from telebot import types

UserAgent().chrome

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("Для всех","Для Алины",row_width=3)

bot = telebot.TeleBot("1935789229:AAEumsN5AhBQqILVcV2QJCzK-MWfx5tpWSQ")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я Кабанчик онлайн! Я выучил таджицкий!",reply_markup=menu)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Для всех":
        if message.chat.id == 1030811973:
            bot.send_message(message.chat.id, "Ты Алина! Меня не заскамишь!",reply_markup=menu)
        else:
            bot.send_message(message.chat.id, "Я кабанчик онлайн! Отправляй мне слово или предложение, а я переведу его на Таджицкий")
    if message.text == "Для Алины":
        if message.chat.id != 1030811973:
            bot.send_message(message.chat.id, "Ты не Алина! Меня не заскамишь!",reply_markup=menu)
        else:
            bot.send_message(message.chat.id, "Идентификация Борна прошла успешно!")
            sleep(1)
            bot.send_message(message.chat.id, "Я кабанчик онлайн! Отправляй мне слово или предложение, а я переведу его на Таджицкий")
            sleep(1)
            bot.send_message(message.chat.id, "А что ты ждала здесь? Ахах Вас заскамили")
            sleep(1)
            bot.send_message(message.chat.id, "И да, похоже на то, что ты вчера сорвалась есть биологические причины)")
    else:
        
        
#        translator= Translator(to_lang="tg")
#        translation = translator.translate(message.text)
        if message.text == "Для всех" or message.text == "Для Алины":
            return
        page = (requests.get("https://ru.contdict.com/перевод/русский-таджикский/"+message.text, headers={'User-Agent': UserAgent().chrome})).text
        start = 68+(page.find('id="translit"'))
        end = page.find('<',start)
        translation = page[start:end]
        if translation == "":
            bot.send_message(message.chat.id, "Не нашёл перевода(")
            return
        bot.send_message(message.chat.id, translation)
bot.polling()
