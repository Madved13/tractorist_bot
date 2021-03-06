import telebot
import constants
import pyowm

bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['pogoda'])
def handle_pogoda(message):

    msg = bot.send_message(message.chat.id, "Какой город Вас интересует?")
    bot.register_next_step_handler(msg,city)
def city(message):
    try:
        city = message.text
        owm = pyowm.OWM(constants.owmkey, language='ru')
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        temperarure = w.get_temperature('celsius')['temp']

        bot.send_message(message.chat.id,"В городе " + city + " сейчас температура: " + str(temperarure) + " по цельсию")
        bot.send_message(message.chat.id,w.get_detailed_status())
    except :
        bot.send_message(message.chat.id, "Не знаю такой город")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if "триста" in message.text:
        bot.send_message(message.chat.id, "Отсоси у тракториста!")
    elif message.text == "куда отправиться?":
        bot.send_location(message.chat.id, 26.0266276,101.6957962)

while True:

    try:

        bot.polling(none_stop=True)

    # ConnectionError and ReadTimeout because of possible timout of the requests library

    # TypeError for moviepy errors

    # maybe there are others, therefore Exception

    except Exception as e:

        logger.error(e)

        time.sleep(15)