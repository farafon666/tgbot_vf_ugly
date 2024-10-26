import json
import requests
import config
import telebot

#init
bot = telebot.TeleBot(config.TOKEN)
app_id = config.OPEN_WEATHER_APP_ID

# function for getting data from API
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={app_id}'

    weather_data = requests.get(url).json()

    if weather_data['cod'] == '404':
        return f'Город "{city}" не найден.'

    # for testing
    weather_data_structure = json.dumps(weather_data, indent=2)
    print(weather_data_structure)

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    return f'Сейчас в городе {city} {str(temperature)} °C.\nОщущается как {str(temperature_feels)} °C.'

# message handler
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши название города, что бы узнать какая там погода.')
    else:
        data = get_weather(message.text)
        bot.send_message(message.from_user.id, data)

# bot start
bot.polling(none_stop=True, interval=0)