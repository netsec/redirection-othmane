from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api import Card, Sms, Info, Analytics
import api

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Card, '/carte')
api.add_resource(Info, '/info')
api.add_resource(Sms, '/sms')
api.add_resource(Analytics, '/analytics')

if __name__ == '__main__':
    app.run()
