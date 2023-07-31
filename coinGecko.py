import requests
import json

t = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").text
t = json.loads(t)
price= int(t['bitcoin']['usd'])
print(price)