from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonpify
from flask import Flask, request, jsonify
import requests

# when a request is made to the reverse proxy, it will forward the request to the backend server (localhost:5002) 
# and return the response to the proxy (localhost:5000) and then to the client (browser)

app = Flask(__name__)
api = Api(app)
CORS(app)

class HelloWorld(Resource):
    def get(self):
        print(" GET Response sent to the client: ")
        return {'about': 'get'}
    
    def post(self):
        some_json = request.get_json()
        print("POST Response sent to the client: ")
        return {'about': some_json}, 201
    
    def put(self):
        print("PUT Response sent to the client: ")
        return {'about': 'put'}
    
    def delete(self):
        print("DELETE Response sent to the client: ")
        return {'about': 'delete'}

    def patch(self):
        print("PATCH Response sent to the client: ")
        return {'about': 'patch'}

class Backend(Resource):
    def get(self):
        # return {'result': 'backend'}
        return requests.get('http://localhost:5002').json()

api.add_resource(HelloWorld, '/')
api.add_resource(Backend, '/backend')

if __name__ == '__main__':
    app.run(port='5002')