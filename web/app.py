"""
Registration of a user 0 tokens
Each user gets 10 tokens
Store a sentence on our database for 1 token
Retrieve his stored sentence on out database for 1 token
"""
from flask import Flask
from flask_restful import Api
from resources import Register, Store, Get

app = Flask(__name__)
api = Api(app)


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')



if __name__=="__main__":
    app.run(host='0.0.0.0')