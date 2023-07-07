import requests 
import Code as c
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

api_url="https://api.coingecko.com/api/v3/simple/price"


#Pull the prices
def get_crypto_price(coin_id):
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    price = data[coin_id]['usd']
    return price