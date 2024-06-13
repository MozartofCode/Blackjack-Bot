from model.game_model import game_state
from Bots.game import bot1_playing


def get_game_state():
    return game_state.to_dict()

def bot1_play():
     bet = game_state.bot1.bet(game_state)
     bot1_playing(game_state.bot1, game_state.house, game_state, bet)