from flask import Flask, jsonify, request
from controller.game import get_game_state
from controller.player import handle_player_action
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line

@app.route('/game-state', methods=['GET'])
def game_state():
    return jsonify(get_game_state())

@app.route('/player-action', methods=['POST'])
def player_action():
    data = request.get_json()
    player_id = data['playerId']
    action = data['action']
    return jsonify(handle_player_action(player_id, action))

if __name__ == '__main__':
    app.run(debug=True)
