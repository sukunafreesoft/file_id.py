import telebot

TOKEN = "7947291291:AAGmeyDhhjoIwRb0eetSPJunsa224mTdMdw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Отправьте файл (документ, видео, фото или аудио), чтобы получить его ID.")

@bot.message_handler(content_types=["document", "video", "photo", "audio"])
def get_file_id(message):
    if message.document:
        bot.send_message(message.chat.id, f"📁 File ID: `{message.document.file_id}`\n🔗 Unique ID: `{message.document.file_unique_id}`", parse_mode="Markdown")
    elif message.video:
        bot.send_message(message.chat.id, f"🎥 File ID: `{message.video.file_id}`\n🔗 Unique ID: `{message.video.file_unique_id}`", parse_mode="Markdown")
    elif message.photo:
        bot.send_message(message.chat.id, f"🖼️ File ID: `{message.photo[-1].file_id}`\n🔗 Unique ID: `{message.photo[-1].file_unique_id}`", parse_mode="Markdown")
    elif message.audio:
        bot.send_message(message.chat.id, f"🎵 File ID: `{message.audio.file_id}`\n🔗 Unique ID: `{message.audio.file_unique_id}`", parse_mode="Markdown")


bot.polling(none_stop=True)
