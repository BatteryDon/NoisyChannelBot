import telebot

token='7111958435:AAEismGDGX3LMqPhsnEYJo_q4TtcSC7izME'

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id,"Привет, Друзья!")
bot.infinity_polling()
