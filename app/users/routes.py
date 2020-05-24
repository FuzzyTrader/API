from app.users import users
from flask import Flask, jsonify, request
from app import mongo, flask_bcrypt, app
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity)

@users.route("/ping", methods = ["GET"])
def ping():
    return jsonify({
        "success" : True,
        "response" : "pong!"
    }), 200

@users.route("/register", methods = ["POST"])
def register():
    users = mongo.db.users

    existing_user = users.find_one({"username" : request.json["username"]})

    if existing_user is None:
        hashpass = flask_bcrypt.generate_password_hash(request.json["password"])

        users.insert_one({
            "username" : request.json["username"],
            "password" : hashpass
        })
        
        return jsonify({
            "success"  : True,
            "response" : "User created!"
        }), 200
    
    return jsonify({
        "success"  : False,
        "response" : "User already exists!"
    }), 400

@users.route("/login", methods = ["POST"])
def login():
    user = mongo.db.users.find_one({"username" : request.json["username"]})

    if flask_bcrypt.check_password_hash(user["password"], request.json["password"]):
        access_token = create_access_token(identity=request.json)

        logged_user = {
            "token"   : access_token
        }

        return jsonify({
            "success" : True,
            "data"    : logged_user
        }), 200
    
    return jsonify({
        "success" : False,
        "response": "Invalid username or password!"
    }), 401