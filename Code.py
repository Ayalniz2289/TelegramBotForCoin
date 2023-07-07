from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Commands as c
TOKEN = "6375556542:AAF3_hgHVZzrf5XKEDXd9Z9Odxdvp64a4AA"

print("Bot çalışmaya başladı!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    #Start command
    dp.add_handler(CommandHandler("start", c.start_command))
    #Wrong command
    dp.add_handler(MessageHandler(Filters.text,c.wrong_command))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()