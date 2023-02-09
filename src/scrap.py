"""
Scrap function from exchange
"""
import requests
from datetime import datetime

from settings import config


def get_ticker_btc_usdt_sell() -> str:
    """
    :return: Time and sell BTC-USDT price
    """
    request = requests.get(config.API_TICKER_BTC_USDT_URL)
    response = request.json()
    sell_price = response["btc_usdt"]["sell"]

    return f"{datetime.now().strftime('%Y-%m-%d %H-%M')}\nSell BTC price: {sell_price}"


def get_ticker_btc_usdt_buy() -> str:
    """
    :return: Time and buy BTC price
    """
    request = requests.get(config.API_TICKER_BTC_USDT_URL)
    response = request.json()
    buy_price = response["btc_usdt"]["buy"]

    return f"{datetime.now().strftime('%Y-%m-%d %H-%M')}\nBuy BTC price: {buy_price}"


def get_ticker_eth_usdt_sell() -> str:
    """
    :return: Time and sell ETH price
    """
    request = requests.get(config.API_TICKER_ETH_USDT_URL)
    response = request.json()
    sell_price = response["eth_usdt"]["sell"]

    return f"{datetime.now().strftime('%Y-%m-%d %H-%M')}\nSell ETH price: {sell_price}"


def get_ticker_eth_usdt_buy() -> str:
    """
    :return: Time and buy ETH price
    """
    request = requests.get(config.API_TICKER_ETH_USDT_URL)
    response = request.json()
    buy_price = response["eth_usdt"]["buy"]

    return f"{datetime.now().strftime('%Y-%m-%d %H-%M')}\nBuy ETH price: {buy_price}"
