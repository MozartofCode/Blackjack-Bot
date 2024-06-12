# @Author: Bertan Berker
# @Filename: Bot2.py
# Bot2 is an AI bot that makes decisions and bettings based on a neural network and the .csv dataset
# that I generated with the moves of bot1

from  Bots.AI_Models.NN import predict_move
import math
import pandas as pd
import tensorflow as tf
import os

class Bot2:
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.hand2 = []

        # Get the absolute path of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the model file
        model_path = os.path.join(current_dir, '../AI_Models/blackjack_model_bot2.h5')
        df_path = os.path.join(current_dir, '../AI_Models/blackjack_dataset.csv')


        self.model = tf.keras.models.load_model(model_path)
        self.df = pd.read_csv(df_path)


    def play(self, player_hand, house_upcard, count, bet, is_initial):
        if is_initial:
            move = predict_move(player_hand, house_upcard, count, bet, self.model, self.df)
            return move
                
        # Hits if < 17 as a bot if not initial hand
        else:
            if self.calculate_hand_val() < 17:
                return "H"
            else:
                return "S"


    def play_2(self, player_hand, house_upcard, count, bet, is_initial):
        
        if is_initial:
            move = predict_move(player_hand, house_upcard, count, bet, self.model, self.df)
            return move
                
        # Hits if < 17 as a bot if not initial hand
        else:
            if self.calculate_hand_val_2() < 17:
                return "H"
            else:
                return "S"


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
    
    
    # Same as Hit move but for adding a card to the bot2's hand2 (after split)
    # :param card: card to add
    def hit_2(self, card):
        self.hand2.append(card)

    
    # Stand move in blackjack
    def stand(self):
        return


    # Double is implemented using hit in game
    # Split is implemented using a combination of hit and gameplay file in game


    # Surrender move in Blackjack where player gives up half of their bet
    # :param bet: bot1's bet for that hand
    def surrender(self, bet):
        self.lose_money(bet//2)
        
    
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
    
    
    # This function is used for calculating the value of bot2's hand2 (after splitting)
    def calculate_hand_val_2(self):
        
        value = 0
        aces = 0
        
        for card in self.hand2:
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


    # Takes money from bot2's account (house won)
    # :param loss: House's loss 
    def lose_money(self, loss):
        self.money -= loss
    

    # Give money to Bot2 (house lost)
    # :param gain: money gained from other player
    def gain_money(self, gain):
        self.money += gain