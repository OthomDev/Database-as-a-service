from flask import Flask, jsonify, request
from flask_restful import Resource
from utils import verifyPw, countTokens
from pymongo import MongoClient
import bcrypt

client = MongoClient("mongodb://db:27017")
db = client.SentecesDatabase
users = db["Users"]



#Register

class Register(Resource):
    def post(self):

        # step 1: is to get posted data by the user
        postedData = request.get_json()
        # Step 2: read the data from the request
        # We are assuming that the username & password are always inserted
        username = postedData["username"]
        password = postedData["password"]
        # step 2 store username and password into the SentenceDatabase
        # we will store the password with hash method with py-bcrypt
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        # Store username and pw into the SentencesDatabase
        users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 6

        })
        retJson = {
            "status": 200,
            "msg": "You have successfully signed up for the API"
        }
        return jsonify(retJson)





#Store










class Store(Resource):
    def post(self):
        # Step 1: Get the posted data
        postedData = request.get_json()
        # Step 2: read the data from the request
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]

        # Step 3: Verify the username and password match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302,
                "Error": "User name or Password is incorrect"
            }
            return jsonify(retJson)
        # Step 4: Verify if the user has enough tokens
        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status": 303,
                "Error": "Not Enough Tokens, Please get more tokens, and try later"
            }
            return jsonify(retJson)    
        # Step 5: Store the senetece, take one token away and return 200
        users.update_one({
            "Username": username
        },
        {
            "$set": {
                "Sentence": sentence,
                "Tokens": num_tokens-1
            }
        })
        retJson = {
            "status": 200,
            "msg": "Sentence is saved succufully"
        }
        return jsonify(retJson)




#Retrieve

class Get(Resource):
    def post(self):

        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302,
                "Error": "User name or Password is incorrect"
            }
            return jsonify(retJson)
        
        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status": 303,
                "Error": "Not Enough Tokens, Please get more tokens, and try later"
            }
            return jsonify(retJson)
        
        # Make the user pay:

        users.update_one({
            "Username": username
        },
        {
            "$set": {
                "Tokens": num_tokens-1
            }
        })
            
        sentence = users.find({
            "Username": username
        })[0]["Sentence"]

        retJson = {
            "Status": 200,
            "msg": sentence
        }
        return jsonify(retJson)
