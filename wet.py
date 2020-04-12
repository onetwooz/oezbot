import pyowm
import telebot

owm = pyowm.OWM('1d98b7784fc6615b03ed79fd09e02050')
bot = telebot.TeleBot('T1035803976:AAGir0Ep1c21B8zwh8Vnu8DWDWWj78EEd_8')

@bot.message_handler(content_types=['text'])
def send_echo(message):
  observation = owm.weather_at_place('London,GB')
  w = observation.get_weather()
  temp = w.get_temperature('celsius')["temp"]
  if message.text.lower() == "расклад"
      bot.send_message(message.chat.id, str(temp))
    
bot.polling(none_stop = True)    
