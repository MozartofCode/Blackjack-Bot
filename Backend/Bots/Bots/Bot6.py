# @Author: Bertan Berker
# @Filename: Bot6.py
# This bot makes decisions based on reinforcement learning


# Example usage:
# predicted_move = predict_move(observation, q_table)
# print(f"Predicted Move: {predicted_move}")
# 1 hit, 0 stand

from  Bots.AI_Models.Q_Learning import predict_move
import os
import math
import numpy as np

class Bot6:
    def __init__(self, money):
        self.money = money
        self.hand = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        q_table_path = os.path.join(current_dir, '../AI_Models/q_table_blackjack.npy')
        self.q_table = np.load(q_table_path)


    def play(self, player, house_upcard):
        
        # Getting the reusable ace from player
        usable_Ace = 0
        for card in player.hand:
            if "Ace" in card:
                usable_Ace = 1

        house_upcard = house_upcard.split(" of ")[0]

        # Processing and getting the value of the upcard of the house
        if house_upcard == "Ace":
            house_upcard = 1
        elif house_upcard in ["King", "Queen", "Jack", "10"]:
            house_upcard = 10
        else:
            house_upcard = str(house_upcard)

        observation = (player.calculate_hand_val(), int(house_upcard), usable_Ace)
        move = predict_move(observation, self.q_table)

        if move == 0:
            return "S"
        
        elif move == 1:
            return "H"
    

    
    # This function bets for bot2
    # :param game: the Game class
    # :return: the bet
    def bet(self, game):
        return self.betting_strategy(self.money, self.get_true_count(game))


    # Calculates the True Count based on 5 decks
    # True Count = Running Count / Number of Decks Remaining.
    # :param game: the Game class
    # :return: true count
    def get_true_count(self, game):
        running_count = game.card_count
        decks_remaining = math.ceil(len(game.deck.cards)/52)
        return running_count//decks_remaining


    # Example Betting Strategy based on Hi-Lo Card Counting
    # True Count ≤ +1: Bet $10.
    # True Count +2 to +3: Bet $20-$40.
    # True Count +4 to +5: Bet $50-$80.
    # True Count ≥ +6: Bet $100 or more.
    # :param money: How much money the player has
    # :param count: the card count
    # :return: how much to bet
    def betting_strategy(self, money, count):

        if money < 10:
            return money
        
        elif count <= 1:
            return 10
        
        elif money < 20:
            return money

        elif count == 2:
            return 20

        elif money < 50:
            return money

        elif count == 3:
            return 50

        elif money < 100:
            return money

        elif count == 4:
            return 100
        
        elif money < 200:
            return money

        elif count == 5:
            return 200
        
        elif money < 500:
            return money
        
        elif count == 6:
            return 500

        elif money < 1000:
            return money
        
        else:
            return 1000




    # Hit move in blackjack, adds a card to the bot2's hand
    # :param card: card to add
    def hit(self, card):
        self.hand.append(card)
    
    # Stand move in blackjack
    def stand(self):
        return
        
    
    # This function is used for calculating the value of bot2's hand
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
    

    # Checks if the value of bot2's hand is over 21 in which case it loses
    def is_over_21(self):
        if self.calculate_hand_val() > 21:
            return True
        return False                


    # Checks if the value of bot2's hand is 21 in which case it's blackjack
    def is_21(self):
        return self.calculate_hand_val() == 21


    # Takes money from bot1's account (house won)
    # :param loss: House's loss 
    def lose_money(self, loss):
        self.money -= loss
    

    # Give money to Bot1 (house lost)
    # :param gain: money gained from other player
    def gain_money(self, gain):
        self.money += gain
    