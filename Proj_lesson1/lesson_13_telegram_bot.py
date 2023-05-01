# Telegram bot
# t.me/prjctr_gifs_bot
import telebot


key = "5890817708:AAHgKXR_2ydpBXloPLxzKQqkto2-3gzXmak"
bot = telebot.TeleBot(key)

@bot.message_handler(content_types=['text'])
def action(message: telebot.types.Message):
    print(message)
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()


# Full (get GIF for word)
# from random import randint
# import requests
# import telebot
#
#
# API_KEY = "4hBaD17Isr71fBi1P9cEKoNpwM7wk9Fj"
# API_URL = f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}"
#
# key = "5890817708:AAHgKXR_2ydpBXloPLxzKQqkto2-3gzXmak"
# bot = telebot.TeleBot(key)
# def search_gifs(query, limit=25, offset=0, rating="g", lang="en"):
#     try:
#         resp = requests.get(f"{API_URL}&q={query}&limit={limit}&offset={offset}&rating={rating}&lang={lang}")
#         resp.raise_for_status()
#         data = resp.json()["data"]
#         return [gif["images"]["downsized_medium"]["url"] for gif in data]
#     except (requests.exceptions.RequestException, KeyError, requests.exceptions.HTTPError) as e:
#         print(f"Error: {e}")
#         return []
#
# @bot.message_handler(content_types=['text'])
# def send_gif(message: telebot.types.Message):
#     word = message.text
#     gifs = search_gifs(word)
#     if gifs:
#         # bot.send_animation(message.chat.id, gifs[0])
#         # bot.send_animation(message.chat.id, gifs[randint(0, 25)])
#         bot.send_video(message.chat.id, gifs[randint(0, 25)])
#     else:
#         bot.reply_to(message, f"Sorry, I couldn't find a GIF for '{word}'.")
#
# bot.polling()