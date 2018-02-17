import telebot
import constants
bot = telebot.TeleBot(constants.token)

#upd = bot.get_updates()

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if "триста" in message.text:
        bot.send_message(message.chat.id, "Отсоси у тракториста!")
    elif message.text == "куда отправиться?":
        bot.send_location(message.chat.id, 26.0266276,101.6957962)


bot.polling(none_stop=True, interval=0)