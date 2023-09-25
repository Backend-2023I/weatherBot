from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
import os 
from main import getWeather

TOKEN = os.environ["TOKEN"]
def start(update:Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id

    samarkand  = KeyboardButton(text="Samarkand")
    tashkent = KeyboardButton(text="Tashkent")

    keyboard = ReplyKeyboardMarkup([[samarkand, tashkent]], resize_keyboard=True)
    bot.sendMessage(chat_id, "hi", reply_markup=keyboard)

def weather(update: Update, context: CallbackContext):
    bot = context.bot
    city = update.message.text
    chat_id = update.message.chat.id

    weather_data = getWeather(city)
    cod = weather_data.get('cod')

    if cod == 200:
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        wind = weather_data['wind']['speed']
        name = weather_data['name']

        text = f"City: {name}\nDescription: {description}\nTemprature: {int(temp)-273}°C\nWind: {wind}m/s"
    else:
        text = "city not found"
    
    bot.sendMessage(chat_id, text)

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, weather))

updater.start_polling()
updater.idle()