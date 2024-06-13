from flask import Flask, jsonify, request
from controller.controller import get_game_state, bot1_play
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/game-state', methods=['GET'])
def game_state():
    return jsonify(get_game_state())


# Example route to handle bot action
@app.route('/bot1-action', methods=['POST'])
def bot1_action():
    bot1_play()
    return jsonify(get_game_state()), 200



if __name__ == '__main__':
    app.run(debug=True)
