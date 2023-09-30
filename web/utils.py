from pymongo import MongoClient
import bcrypt


client = MongoClient("mongodb://db:27017")
db = client.SentecesDatabase
users = db["Users"]





def verifyPw(username, password):
    hashed_pw = users.find({
        "Username": username
    })[0]["Password"]
    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False
    



    
def countTokens(username):
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]
    return tokens