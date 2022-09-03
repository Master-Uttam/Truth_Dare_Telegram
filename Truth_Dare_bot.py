import telebot
from data import token, quest, truth_items, dare_items
import random

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=["t", "q", "d"])
def send_message(message):
    try:
        reply_to_message = str(message.reply_to_message.from_user.username)
        if reply_to_message == "None":
            reply_to_message = str(message.reply_to_message.from_user.first_name)
        reply_to(message, reply_to_message)

    except:
        if message.text.startswith('/q'):
            bot.reply_to(message, random.choice(quest))

        elif message.text.startswith('/d'):
            bot.reply_to(message, random.choice(dare_items))

        elif message.text.startswith('/t'):
            bot.reply_to(message, random.choice(truth_items))


def reply_to(message, reply_to_message):
    if message.text.startswith('/q'):
        bot.reply_to(message, f"{random.choice(quest)} @{reply_to_message}")

    elif message.text.startswith('/d'):
        bot.reply_to(message, f"{random.choice(dare_items)} @{reply_to_message}")

    elif message.text.startswith('/t'):
        bot.reply_to(message, f"{random.choice(truth_items)} @{reply_to_message}")


bot.infinity_polling()
# #message.from_user.id
# message.from_user.first_name
# message.from_user.last_name
# message.from_user.username
