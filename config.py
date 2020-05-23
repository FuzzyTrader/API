import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

class Config(object):
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'), 10)

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True