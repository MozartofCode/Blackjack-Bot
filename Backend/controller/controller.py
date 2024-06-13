from model.game_model import game_state
from Bots.game import bot1_playing
from Bots.game import bot2_playing
from Bots.game import bot3_playing
from Bots.game import bot4_playing
from Bots.game import bot5_playing
from Bots.game import bot6_playing


def get_game_state():
    return game_state.to_dict()

def bot1_play():
     bet = game_state.bot1.bet(game_state)
     bot1_playing(game_state.bot1, game_state.house, game_state, bet)

def bot2_play():
     bet = game_state.bot2.bet(game_state)
     bot2_playing(game_state.bot2, game_state.house, game_state, bet)


def bot3_play():
     bet = game_state.bot3.bet(game_state)
     bot3_playing(game_state.bot3, game_state.house, game_state, bet)


def bot4_play():
     bet = game_state.bot4.bet(game_state)
     bot4_playing(game_state.bot4, game_state.house, game_state, bet)


def bot5_play():
     bet = game_state.bot5.bet(game_state)
     bot5_playing(game_state.bot5, game_state.house, game_state, bet)


def bot6_play():
     bet = game_state.bot6.bet(game_state)
     bot6_playing(game_state.bot6, game_state.house, game_state, bet)

def player_play(move):
     if move == "H":
          return