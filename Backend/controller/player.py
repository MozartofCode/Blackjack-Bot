# @ Author: Bertan Berker
# @ Language: Python - Flask framework

from controller.game import get_game_state
from Bots.Player import Player

def handle_player_action(player, action):

    if action == 'hit':
        player.hit()
    elif action == 'stand':
        player.stand()
    elif action == 'stand':
        player.stand()
    elif action == 'stand':
        player.stand()
    elif action == 'stand':
        player.stand()

    return get_game_state()







# # Import necessary modules
# import requests
# from flask import Flask, jsonify
# from flask_cors import CORS


# # Create a Flask app
# app = Flask(__name__)
# CORS(app)

# @app.route('/player/hit', methods=['POST'])
# def hit():
#     return


# @app.route('/player/hit', methods=['POST'])
# def stay():
#     return

# @app.route('/player/hit', methods=['POST'])
# def surrender():
#     return

# @app.route('/player/hit', methods=['POST'])
# def double():
#     return

# @app.route('/player/hit', methods=['POST'])
# def split():
#     return



