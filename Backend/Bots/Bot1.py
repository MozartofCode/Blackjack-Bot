# Basic Strategy & Hi-Lo Card Counting

import math

# Based on 5 decks
# True Count = Running Count / Number of Decks Remaining.
def get_true_count(game):

    running_count = game.return_count()
    decks_remaining = math.ceil(len(game.deck.cards)/52)

    return running_count//decks_remaining


#TODO: BETTING STRATEGY

# Example Betting Strategy
# Let’s assume your betting unit (minimum bet) is $10:

# True Count ≤ +1: Bet $10.
# True Count +2 to +3: Bet $20-$40.
# True Count +4 to +5: Bet $50-$80.
# True Count ≥ +6: Bet $100 or more.
