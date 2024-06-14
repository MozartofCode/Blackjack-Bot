from model.game_model import game_state

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
