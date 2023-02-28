import redis
from flask import Flask,render_template
from os import environ
from requests import get as requestGet

REDIS_HOST = environ.get('REDIS_HOST')
REDIS_PORT = environ.get('REDIS_PORT')
SERVER_PORT = environ.get('SERVER_PORT')

app = Flask(__name__)
cache = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT))

cryptoApiAvg = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=9'
cryptoApiCurrentPrice = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'


# return the current price of BTC
def getCurrentPrice():
    response = requestGet(cryptoApiCurrentPrice)
    price = response.json()['USD']
    cache.set('currentPrice', price)
    return price


# return the avaerage of the last 10 minutes of BTC price
def getAvgPrice():
    response = requestGet(cryptoApiAvg)
    candles = response.json()['Data']['Data']
    sum = 0
    for candle in candles:
        sum += candle['close']

    avg = sum / len(candles)
    cache.set('avgPrice', avg)

    return avg


@app.route('/')
def getBtcPrice():
    return render_template('index.html',CurrentPrice= cache.get('currentPrice') ,AvgPrice = cache.get('avgPrice'))


if __name__ == '__main__':
    app.run(port=int(SERVER_PORT), host='0.0.0.0')
