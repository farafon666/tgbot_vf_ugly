import config
import telebot

# Присваивание токена
bot = telebot.TeleBot(config.TOKEN)

# Функция повтора сообщений
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

# Цикл
bot.polling(none_stop=True)