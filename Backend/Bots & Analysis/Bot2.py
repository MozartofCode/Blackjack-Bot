# @Author: Bertan Berker
# @Filename: Bot2.py
# Bot2 is an AI bot that makes decisions and bettings based on a neural network and the .csv dataset
# that I generated with the moves of bot1

from NN import predict_move, create_NN_model

class Bot2:
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.hand2 = []
        self.model = create_NN_model()


    def play(self, player_hand, house_upcard, count, bet, is_initial):
        if is_initial:
            move = predict_move(player_hand, house_upcard, count, bet, self.model)
            return move
                
        # Hits if < 17 as a bot if not initial hand
        else:
            if self.calculate_hand_val() < 17:
                return "H"
            else:
                return "S"

    #TODO
    def play2(self, player_hand, house_upcard, count, bet, is_initial):
        if is_initial:
            move = predict_move(player_hand, house_upcard, count, bet, self.model)
            return move
                
        # Hits if < 17 as a bot if not initial hand
        else:
            if self.calculate_hand_val2() < 17:
                return "H"
            else:
                return "S"


    
    def hit(self, card):
        self.hand.append(card)
        
    def hit_2(self, card):
        self.hand2.append(card)

    def calculate_hand_val(self):
        return    
    






