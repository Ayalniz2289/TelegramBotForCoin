from telegram.ext import Updater

def start_command(update, context):
  message = "Welcome, I am created by Ali Yalnız. I am ready to give you instant prices of crypto markets."
  
  return update.message.reply_text(message)

def wrong_command(update,context):
  message="There is currently no functionality for this command. Please try different commands!"
  return update.message.reply_text(message)