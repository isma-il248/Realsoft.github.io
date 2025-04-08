from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


api_id = 28935504         # my.telegram.org'dan al
api_hash = "c72eedf076dc8484916ef729a24fa4c2"
bot_token = "7846819154:AAGiQMKt66bYMxkuQw7H_OofbkDyJuURfe4"

# Botu başlat
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(_, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Göz at 🚀", web_app=WebAppInfo(url="https://isma-il248.github.io/Realsoft.github.io/"))]
    ])
    await message.reply("Hoş geldin dostum! 👋\nBilgi almak için görüntüle:", reply_markup=keyboard)

print("Bot hazır, internetin tozunu almaya gidiyor... 🧹")
app.run()
