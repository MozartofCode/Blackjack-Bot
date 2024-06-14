from flask import Flask, jsonify, request
from controller.controller import get_game_state, player_play, player_betting
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


@app.route('/player-bet', methods=['POST'])
def player_bet():
    request_data = request.get_json()
    print(request_data)
    bet = int(request_data['bet'])
    player_betting(bet)
    return jsonify(get_game_state()), 200



if __name__ == '__main__':
    app.run(debug=True)
