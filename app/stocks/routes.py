from app.stocks import stocks
from flask import Flask, jsonify, request

@stocks.route("/ping", methods = ["GET"])
def ping():
    return jsonify({"success" : True,
                    "response" : "pong!"
                    }), 200