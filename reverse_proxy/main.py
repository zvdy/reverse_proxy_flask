from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonpify
from flask import Flask, request, jsonify
import requests

# reverse proxy that acts as a gateway to the backend server (localhost:5002) 

app = Flask(__name__)
api = Api(app)
CORS(app)

# forward the request to the backend server (localhost:5002)
# and return the response to the client (browser) when the backend server sends a response back to the reverse proxy

class sendgetResponse(Resource):
    def get(self):
        return requests.get('http://localhost:5002').json()


class sendpostResponse(Resource):
    def post(self):
        some_json = request.get_json()
        return requests.post('http://localhost:5002', json=some_json).json()


class sendputResponse(Resource):
    def put(self):
        return requests.put('http://localhost:5002').json()


class senddeleteResponse(Resource):
    def delete(self):
        return requests.delete('http://localhost:5002').json()



class sendBackendResponseToClient(Resource):
    def get(self):
        return requests.get('http://localhost:5002/backend').json()



api.add_resource(sendgetResponse, '/')
api.add_resource(sendpostResponse, '/')
api.add_resource(sendputResponse, '/')
api.add_resource(senddeleteResponse, '/')
api.add_resource(sendBackendResponseToClient, '/backend')

if __name__ == '__main__':
    app.run(port='5000')
    
