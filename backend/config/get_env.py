import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

_env = os.environ.get

VUE_APP_API_URL = _env('VUE_APP_API_URL')
POSTGRES_HOST = _env('POSTGRES_HOST')
POSTGRES_USER = _env('POSTGRES_USER')
POSTGRES_DB = _env('POSTGRES_DB')
POSTGRES_PASSWORD = _env('POSTGRES_PASSWORD')
POSTGRES_PORT = _env('POSTGRES_PORT')
