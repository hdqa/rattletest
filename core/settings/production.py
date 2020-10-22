from decouple import config

from core.settings.base import *

SECRET_KEY = config("SECRET_KEY")
