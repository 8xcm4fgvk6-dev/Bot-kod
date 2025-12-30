import os
from telebot import TeleBot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
ADMIN_ID = int(os.environ.get("ADMIN_ID"))

bot = TeleBot(BOT_TOKEN)

codes = {
    "A123": "https://t.me/video_link1",
    "B456": "https://t.me/video_link2"
}

@bot.message_handler(commands=['start'])
def start(message):
    try:
        user_status = bot.get_chat_member(CHANNEL_ID, message.from_user.id).status
        if user_status == 'left':
            bot.send_message(message.chat.id, f"Iltimos, kanalga obuna bo'ling: {CHANNEL_ID}")
        else:
            bot.send_message(message.chat.id, "Salom! Kodni kiriting:")
    except:
        bot.send_message(message.chat.id, "Kanal bilan bog‘liq xatolik. Adminga murojaat qiling.")

@bot.message_handler(func=lambda message: True)
def code_check(message):
    if message.text in codes:
        bot.send_message(message.chat.id, f"Video link: {codes[message.text]}")
    else:
        bot.send_message(message.chat.id, "Kod topilmadi. Tekshirib qaytadan yozing.")

bot.infinity_polling()
