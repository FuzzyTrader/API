from app.stocks import stocks
from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required
from app import mongo

@stocks.route("/ping", methods = ["GET"])
def ping():
    return jsonify({
        "success" : True,
        "response" : "pong!"
    }), 200

@stocks.route("/add", methods = ["POST"])
@jwt_required
def add_stocks():
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

@stocks.route("/wallet", methods=["GET"])
@jwt_required
def get_wallet():
    stocks = mongo.db.stocks

    user_stocks = stocks.find({ "username" : request.args.get("username")})
    list_stocks = list(user_stocks)

    if len(list_stocks) == 0:
        return jsonify({
            "success" : False,
            "response" : "No stock records were found for this user!"
        }), 404
    
    result = []

    for stock in list_stocks:
        result.append({
            "code"  : stock["stock"],
            "amount": stock["amount"]
        })
    
    return jsonify({
        "success" : True,
        "data"    : result
    }), 200