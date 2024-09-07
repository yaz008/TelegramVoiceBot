from dotenv import load_dotenv
if not load_dotenv('.env'):
	raise Exception('Unable to load .env file')

from os import getenv
from telebot import TeleBot

bot: TeleBot = TeleBot(token=getenv(key='TELEGRAM_API_KEY'),
                       parse_mode='Markdown',
                       skip_pending=True,
                       threaded=False)