from telegram.ext import Updater

def start_command(update, context):
  message = "Merhaba ben Ali, sana son dakika haberlerini getirmeye çalışacağım"
  
  return update.message.reply_text(message)

def wrong_command(update,context):
  message="Şu an bu komut için herhangi bir işlevim bulunmuyor lütfen farklı komutları deneyiniz !"
  return update.message.reply_text(message)