import os
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))

APP_PORT = os.getenv('APP_PORT')
APP_HOST = '127.0.0.1'

#POSTGRES
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

POSTGRES_URL = f'postgresql+psycopg2://\
                {POSTGRES_USER}:\
                {POSTGRES_PASSWORD}@\
                {POSTGRES_HOST}:\
                {POSTGRES_PORT}/\
                {POSTGRES_DB}'.replace(" ","")

CENTRIFUGO_HTTP_URL = os.getenv('CENTRIFUGO_HTTP_URL')
CENTRIFUGO_WS_URL = os.getenv('CENTRIFUGO_WS_URL')
CENTRIFUGO_API_KEY = os.getenv('CENTRIFUGO_API_KEY')
CENTRIFUGO_SECRET = os.getenv('CENTRIFUGO_SECRET')

