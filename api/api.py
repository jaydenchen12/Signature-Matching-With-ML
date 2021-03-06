from flask import Flask, jsonify, request
from flask_cors import CORS
from routes import api

app = Flask(__name__)
cors = CORS(app)
api.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
