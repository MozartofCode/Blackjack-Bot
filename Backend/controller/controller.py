from model.game_model import game_state

def get_game_state():
    return game_state.to_dict()

def player_play(move):
     if move == "H":
          return