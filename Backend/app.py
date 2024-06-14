from flask import Flask, jsonify, request
from controller.controller import get_game_state, player_play
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/game-state', methods=['GET'])
def game_state():
    return jsonify(get_game_state())

@app.route('/player-action', methods=['POST'])
def player_action():
    request_data = request.get_json()
    move = request_data['action']
    player_play(move)
    return jsonify(get_game_state()), 200




if __name__ == '__main__':
    app.run(debug=True)
