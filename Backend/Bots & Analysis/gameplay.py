# @Author: Bertan Berker
# @File: gameplay.py 
# This file contains the basic functionality for the gameplay 
# For example: shuffling a deck, distributing cards...

import random
from House import House
from Bot1 import Bot1
from Bot2 import Bot2
from Bot3 import Bot3

# 5 deck of cards (5 x 52 cards)

class Deck:

    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for i in range(5):        
            for suit in suits:
                for rank in ranks:
                    self.cards.append(rank + ' of ' + suit)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    
    def peek_card(self):        # Only for card counting algorithm
        
        if len(self.cards) > 0:
            return self.cards[-1]
        return None


class Game:

    def __init__(self):

        house_money = 10000000
        player_money = 1000

        self.deck = Deck()
        self.deck.shuffle()
        self.card_count = 0     # For card counting purposes
        self.table_money = 0

        self.house = House(house_money)
        self.bot1 = Bot1(player_money)
        self.bot2 = Bot2(player_money)
        self.bot3 = Bot3(player_money)


    # return True if player1 winner
    # return False if player2 winner
    def decide_winner(player1, player2):
        
        if player1.calculate_hand_val() > 21:
            return False
        
        elif player2.calculate_hand_val() > 21:
            return True
        
        elif player1 < player2:
            return False
        
        else:
            return True


    def cards_left_check(self):
        # 20 is a random number since 5 players if each plan to get 5 cards
        if len(self.deck.cards) <= 25:
            # Recreate the deck
            self.deck = Deck
            self.deck.shuffle()
            self.count = 0
        

    def deal_initial_hands(self):

        self.cards_left_check()

        # Each player gets 2 cards
        for _ in range(2):
            self.house.hit(self.deck.deal_card())
            self.bot1.hit(self.deck.deal_card())
            self.bot2.hit(self.deck.deal_card())
            self.bot3.hit(self.deck.deal_card())
    

    def deal_single_card(self, player_name):
        
        self.cards_left_check()
        self.card_count += self.count_card(self.deck.peek_card())

        if player_name == "house":
            self.house.hit(self.deck.deal_card())
        
        elif player_name == "bot1":
            self.bot1.hit(self.deck.deal_card())

        elif player_name == "bot2":
            self.bot2.hit(self.deck.deal_card())

        elif player_name == "bot3":
            self.bot3.hit(self.deck.deal_card())
    
    
    def deal_single_card_2(self, player_name):
        
        self.cards_left_check()
        self.card_count += self.count_card(self.deck.peek_card())

        if player_name == "bot1":
            self.bot1.hit_2(self.deck.deal_card())

        elif player_name == "bot2":
            self.bot2.hit_2(self.deck.deal_card())

        elif player_name == "bot3":
            self.bot3.hit_2(self.deck.deal_card())

    # Hi - Lo Card Counting logic
    # 2-6 is +1
    # 7-9 is 0
    # 10-A is -1
    def count_card(self, card):
        
        if card.split(" of ")[0] in ["Jack", "Queen", "King", "Ace"]:
            return -1
        elif card.split(" of ")[0] in ["7", "8", "9"]:
            return 0
        else:
            return 1
