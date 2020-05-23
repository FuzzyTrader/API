import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

class Config(object):
    MONGO_URI = os.getenv("MONGO_URI")

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True