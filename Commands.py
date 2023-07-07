from telegram.ext import Updater

def start_command(update, context):
  message = "Merhaba ben Ali, sana son dakika haberlerini getirmeye çalışacağım"
  
  return update.message.reply_text(message)

