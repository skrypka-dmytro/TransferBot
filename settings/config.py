"""
Configuration file with bot settings and API keys from third-party services
"""
import os
from dotenv import load_dotenv


# Loading env variables from .env file
load_dotenv(".env")

ENVIRONMENT = os.environ.get('APP_NAME', 'dev')  # Available environments: dev / prod

API_BOT_KEY = os.environ.get("API_BOT_KEY")

APP_NAME = os.environ.get("APP_NAME", "MyApp")

API_INFO_URL = os.environ.get("API_INFO_URL")
API_TICKER_BTC_USDT_URL = os.environ.get("API_TICKER_BTC_USDT_URL")
API_TICKER_ETH_USDT_URL = os.environ.get("API_TICKER_ETH_USDT_URL")
