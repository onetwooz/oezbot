import telebot

bot = telebot.TeleBot('T1035803976:AAGir0Ep1c21B8zwh8Vnu8DWDWWj78EEd_8')

@bot.message_handler(content_types=['text'])
def send_echo(message):
  
  if message.text.lower() == "расклад"
      bot.send_message(message.chat.id, cjcb)
    
bot.polling(none_stop = True)    
