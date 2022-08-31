import telebot

bot = telebot.TeleBot('5468049801:AAEjALJtNUgOH5q65qIYlwKnnaRBZ9PdaP8')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello" or "hello":
        bot.send_message(message.chat.id, "Hi", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id is: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "I dont know", parse_mode='html')


bot.polling(none_stop=True)