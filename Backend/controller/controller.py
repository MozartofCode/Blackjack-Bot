from model.game_model import game_state
from Bots.gameplay import Game

def get_game_state():
    return game_state.to_dict()

def player_play(move):
     if move == "H":
          game_state.deal_single_card("player")
          if game_state.player.calculate_hand_val() >= 21:
               game_state.player.in_game = False
               
     elif move == "S":
          game_state.player.in_game = False

          return

def player_betting(bet):
     print("Player is betting")
     game_state.player.bet(bet)


def house_betting(bet):
     print("House is betting")
     game_state.house.bet(bet)

def house_play():
     game_state.house.play(game_state.player, game_state)
     game_state.house.in_game = False


def initialize_new_round():
     game_state.player.the_bet = 0
     game_state.player.in_game = True
     game_state.player.hand = []
     game_state.house.hand = []
     game_state.house.the_bet = 0
     game_state.house.in_game = True
     
     game_state.deal_initial_hands(True, True, True, True, True, True)
