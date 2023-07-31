from telegram.ext import Updater
import requests

def start_command(update, context):
  message = "Welcome, I am created by Ali Yalnız. I am ready to give you instant prices of crypto markets."
  
  return update.message.reply_text(message)

def wrong_command(update,context):
  message="There is currently no functionality for this command. Please try different commands!"
  return update.message.reply_text(message)

def price_command(update,context):
  message="Please enter the name of the coin you want to see the price of. For example: /price bitcoin"
  coin_id=context.args[0]
  if coin_id:
    api_url=f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd" #coin_id is the coin name
    response = requests.get(api_url)
    response_json = response.json()
    coin_price = response_json[coin_id]["usd"]
    message = f"The price of {coin_id} is {coin_price} USD." 
    return update.message.reply_text(message)
  else:
    message="Please enter the name of the coin you want to see the price of. For example: /price bitcoin"
    return update.message.reply_text(message)
      


 