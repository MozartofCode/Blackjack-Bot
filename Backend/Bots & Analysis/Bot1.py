# Basic Strategy & Hi-Lo Card Counting
# Hits if < 17 as a bot if not initial hand

import math
from Basic_Strategy import apply_basic_strategy

# import basics.py

class Bot1:

    def __init__(self, money):
        self.money = money
        self.hand = []
    
    def init_hand(self):
        self.hand = []

    def play(self, house, player, is_initial):
        
        if is_initial:
            move = apply_basic_strategy(house, player)
            return move
        
        else:
            if self.calculate_hand_val() < 17:
                return "H"
            else:
                return "S"
    
    def bet(self, game):
        return self.betting_strategy(self.money, self.get_true_count(game))

    # Based on 5 decks
    # True Count = Running Count / Number of Decks Remaining.
    def get_true_count(self, game):

        running_count = game.card_count
        decks_remaining = math.ceil(len(game.deck.cards)/52)

        return running_count//decks_remaining

    # Example Betting Strategy
    # Let’s assume your betting unit (minimum bet) is $10:

    # True Count ≤ +1: Bet $10.
    # True Count +2 to +3: Bet $20-$40.
    # True Count +4 to +5: Bet $50-$80.
    # True Count ≥ +6: Bet $100 or more.

    def betting_strategy(self, money, count):

        if money < 10:
            return money
        
        elif count <= 1:
            return 10
        
        elif money < 20:
            return money

        elif count == 2:
            return 20

        elif money < 30:
            return money

        elif count == 3:
            return 30

        elif money < 60:
            return money

        elif count == 4:
            return 60
        
        elif money < 80:
            return money

        elif count == 5:
            return 80
        
        elif money < 150:
            return money

        else:
            return 150
    
    def hit(self, card):
        self.hand.append(card)
 
    def stand(self):
        return
    
    # Double is implemented using hit in gameplay

    def surrender(self, bet):
        self.lose_money(bet/2)
        

    def split(self, card):
        return


















    def calculate_hand_val(self):
        
        value = 0
        aces = 0
        
        for card in self.hand:
            val = card.split(" of ")[0]

            if val in ["Jack", "Queen", "King"]:
                value += 10
            
            elif val == "Ace":
                # Add aces at the end for the proper value calculation
                aces += 1

            else:
                value += int(val)
            
        while aces != 0:
            
            # If adding Ace as 11 makes it > 21 than Ace is 1
            if value + 11 > 21:
                    value += 1
            else:
                value += 11

            aces -= 1

        return value 
    
    def is_over_21(self):
        if self.calculate_hand_val() > 21:
            return True
        return False                

    def is_21(self):
        return self.calculate_hand_val() == 21

    def lose_money(self, loss):
        self.money -= loss
    
    def gain_money(self, gain):
        self.money += gain
    

