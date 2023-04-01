import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

_env = os.environ.get

VUE_APP_API_URL = _env('VUE_APP_API_URL')