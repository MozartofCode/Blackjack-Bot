from flask import Flask, jsonify, request
from controller.controller import get_game_state, bot1_play, bot2_play, bot3_play, bot4_play, bot5_play, bot6_play
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/game-state', methods=['GET'])
def game_state():
    return jsonify(get_game_state())

@app.route('/bot1-action', methods=['POST'])
def bot1_action():
    bot1_play()
    return jsonify(get_game_state()), 200

@app.route('/bot2-action', methods=['POST'])
def bot2_action():
    bot2_play()
    return jsonify(get_game_state()), 200

@app.route('/bot3-action', methods=['POST'])
def bot3_action():
    bot3_play()
    return jsonify(get_game_state()), 200

@app.route('/bot4-action', methods=['POST'])
def bot4_action():
    bot4_play()
    return jsonify(get_game_state()), 200

@app.route('/bot5-action', methods=['POST'])
def bot5_action():
    bot5_play()
    return jsonify(get_game_state()), 200

@app.route('/bot6-action', methods=['POST'])
def bot6_action():
    bot6_play()
    return jsonify(get_game_state()), 200



if __name__ == '__main__':
    app.run(debug=True)
