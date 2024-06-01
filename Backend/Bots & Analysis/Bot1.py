# Basic Strategy & Hi-Lo Card Counting
# Hits if < 17 as a bot if not initial hand



import math
import Basic_Strategy
import basics

# import basics.py

class Bot1:

    def __init__(self, money):
        self.bot = basics.Player(money)
        
    def play(self, house, player_hand, is_initial):
        
        if is_initial:
            move = Basic_Strategy.apply_basic_strategy(house, player_hand)
            return move
        
        else:
            if self.bot.calculate_hand_val() < 17:
                return "H"
            else:
                return "S"
    
    def bet(self, game):
        count = self.get_true_count(game)
        money = self.bot.money
        return self.betting_strategy(money, count)
        

    # Based on 5 decks
    # True Count = Running Count / Number of Decks Remaining.
    def get_true_count(self, game):

        running_count = game.return_count()
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