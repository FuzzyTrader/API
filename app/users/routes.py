from app.users import users
from flask import Flask, jsonify, request
from app import mongo, flask_bcrypt

@users.route("/ping", methods = ["GET"])
def ping():
    return jsonify({"success" : True,
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
        
        return jsonify({"success"  : True,
                        "response" : "User created!"
                        }), 200
    
    return jsonify({"success"  : False,
                    "response" : "User already exists!"
                    }), 400