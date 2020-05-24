from app.stocks import stocks
from flask import Flask, jsonify, request
from app import mongo

@stocks.route("/ping", methods = ["GET"])
def ping():
    return jsonify({
        "success" : True,
        "response" : "pong!"
    }), 200

@stocks.route("/add", methods = ["POST"])
# @jwt_required
def add():
    stocks = mongo.db.stocks

    new_stocks = request.json["stocks"]
    user = request.json["username"]

    for stock in new_stocks:
        existing_stock = stocks.find_one({
            "$and" : [
                { "username" : user },
                { "stock"    : stock["code"] }
        ]})

        if existing_stock is None:
            new_stock = {
                "stock" : stock["code"],
                "amount": stock["amount"],
                "username"  : user
            }
        
            stocks.insert_one(new_stock)
        
        else:
            new_amount = existing_stock["amount"] + stock["amount"]
            stocks.update_one({"_id" : existing_stock["_id"]}, {"$set" : { "amount" : new_amount }})
    
    return jsonify({
        "success" : True,
        "response" : "Stocks were added to wallet!"
    }), 200
