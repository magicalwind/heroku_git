import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eblrusjmnmquxu:3991d130b10cbb6f3b62c7e00fb726eeafc231f3e5c3a2ed1ae480eab1d5bfe3@ec2-18-209-153-180.compute-1.amazonaws.com:5432/d7s5a73883li2a'   # , set the db path, for now, the path of db is the root of app.py
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)




jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':

    app.run(port=5000, debug=True)
