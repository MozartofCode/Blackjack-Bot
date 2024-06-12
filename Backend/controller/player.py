# @ Author: Bertan Berker
# @ Language: Python - Flask framework
#
#

# Import necessary modules
import requests
from flask import Flask, jsonify
from flask_cors import CORS


# Create a Flask app
app = Flask(__name__)
CORS(app)

@app.route('/player/hit', methods=['POST'])
def hit():
    return


@app.route('/player/hit', methods=['POST'])
def stay():
    return

@app.route('/player/hit', methods=['POST'])
def surrender():
    return

@app.route('/player/hit', methods=['POST'])
def double():
    return

@app.route('/player/hit', methods=['POST'])
def split():
    return



