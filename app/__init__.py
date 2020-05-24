from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta, datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

jwt = JWTManager(app)
flask_bcrypt = Bcrypt(app)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(app.config['JWT_ACCESS_TOKEN_EXPIRES'])
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mongo = MongoClient(app.config["MONGO_URI"])

from .users import users
app.register_blueprint(users, url_prefix="/api/users")

from .stocks import stocks
app.register_blueprint(stocks, url_prefix="/api/stocks")