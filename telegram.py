"""
Run this file
"""
import telebot

from settings import config
from src.scrap import (
    get_ticker_btc_usdt_sell,
    get_ticker_btc_usdt_buy,
    get_ticker_eth_usdt_sell,
    get_ticker_eth_usdt_buy,
)

bot = telebot.TeleBot(config.API_BOT_KEY)


@bot.message_handler(commands=["start"])
def start_message(message) -> None:
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name}!"
        f"\nYou can find out the buying and selling rate: BTC-USDT or ETH-USDT"
        f"\nEnter example BTC-USDT (sell or buy)",
    )


@bot.message_handler(content_types=["text"])
def send_message(message) -> None:
    if message.text.lower() == "btc-usdt sell":
        try:
            bot.send_message(message.chat.id, get_ticker_btc_usdt_sell())
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Oops...Something was wrong...")

    elif message.text.lower() == "btc-usdt buy":
        try:
            bot.send_message(message.chat.id, get_ticker_btc_usdt_buy())
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Oops...Something was wrong...")

    elif message.text.lower() == "eth-usdt sell":
        try:
            bot.send_message(message.chat.id, get_ticker_eth_usdt_sell())
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Oops...Something was wrong...")

    elif message.text.lower() == "eth-usdt buy":
        try:
            bot.send_message(message.chat.id, get_ticker_eth_usdt_buy())
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Oops...Something was wrong...")

    else:
        bot.send_message(message.chat.id, "Enter correct command!")


if __name__ == "__main__":
    bot.polling(none_stop=True)
