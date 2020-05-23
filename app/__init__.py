from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

flask_bcrypt = Bcrypt(app)

mongo = MongoClient(app.config["MONGO_URI"])

from .users import users
app.register_blueprint(users, url_prefix="/api/users")

from .stocks import stocks
app.register_blueprint(stocks, url_prefix="/api/stocks")