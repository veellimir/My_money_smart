import os

from dotenv import load_dotenv

load_dotenv()

CONFIG__SECRET_KEY = os.getenv("CONFIG__SECRET_KEY")
CONFIG__DEBUG = os.getenv("CONFIG__DEBUG")

CONFIG__ALLOWED_HOSTS = os.getenv("CONFIG__ALLOWED_HOSTS")