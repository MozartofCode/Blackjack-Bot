from model.game_model import game_state

def get_game_state():
    return game_state.to_dict()

def player_play(move):
     if move == "H":
          game_state.deal_single_card("player")
          print("Player hit")
          print("Player's cards: " + str(game_state.player.hand))
     
     elif move == "S":
          print("Player is staying")
          return

def player_betting(bet):
     print("Player is betting")
     game_state.player.bet(bet)