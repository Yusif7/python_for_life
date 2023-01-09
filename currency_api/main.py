from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests


# Scraping currency from x-rates
def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find('span', class_='ccOutputRslt').get_text()
    currency = currency[:-4]
    return currency


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Currency rate API</h1><p>Example URL: /api/v1/usd-eur</p>"


# <in_cur>-<out_cur> - special syntax using when we need to change currency values in process
# http://127.0.0.1:5000/api/v1/rub-eur - we can change rub and usd any currency what we want
@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    result_dict = {
        "input currency": in_cur,
        "output currency": out_cur,
        "rate": rate
    }

    return jsonify(result_dict)


app.run()
