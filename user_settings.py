import os
import requests

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

settings = {
    "user_currencies": ["USD", "EUR"],
    "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"],
}

currency_list = []
currency_stock = []


def get_current_price(currency):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount=1"

    payload = {}
    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)

    user_currencies = response.json()["query"]["from"]
    price = response.json()["info"]["rate"]
    price = round(price, 2)

    return {"currency": user_currencies, "rate": price}


# print(get_current_price('USD'))


def add_to_list():
    for currency in settings["user_currencies"]:
        currency_list.append(get_current_price(currency))
    return currency_list


# print(add_to_list())


def get_current_stock(sett):
    url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey=PltnhzgjML0noZote0Z2nK8TZYU9t3cw"
    payload = {}

    response = requests.request("GET", url, data=payload)

    result = response.json()

    for stock in result:
        for my_stock in sett["user_stocks"]:
            if stock["symbol"] == my_stock:
                currency_stock.append(
                    {"stock": stock["symbol"], "price": stock["price"]}
                )
    return currency_stock


# print(get_current_stock(settings))