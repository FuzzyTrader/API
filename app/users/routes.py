from app.users import users
from flask import Flask, jsonify, request

@users.route("/ping", methods = ["GET"])
def ping():
    return jsonify({"success" : True,
                    "response" : "pong!"
                    }), 200