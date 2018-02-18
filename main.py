import telebot
import constants
import pyowm

bot = telebot.TeleBot(constants.token)

#upd = bot.get_updates()

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)
"""
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if "триста" in message.text:
        bot.send_message(message.chat.id, "Отсоси у тракториста!")
    elif message.text == "куда отправиться?":
        bot.send_location(message.chat.id, 26.0266276,101.6957962)
"""
@bot.message_handler(commands=['pogoda'])
def handle_pogoda(message):

    msg = bot.send_message(message.chat.id, "Какой город Вас интересует?")
    bot.register_next_step_handler(msg,city)
def city(message):
    city = message.text
    owm = pyowm.OWM(constants.owmkey)
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperarure = w.get_temperature('celsius')['temp']

    bot.send_message(message.chat.id,"В городе " + city + " сейчас температура: " + str(temperarure) + " по цельсию")


bot.polling(none_stop=True, interval=0)