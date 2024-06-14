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

          print("Print player.in_game=FALSE")
          print(game_state.player.in_game)
          return

def player_betting(bet):
     print("Player is betting")
     game_state.player.bet(bet)