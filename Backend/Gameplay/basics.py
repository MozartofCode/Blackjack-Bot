# @Author: Bertan Berker
# @File: basics.py 
# This file contains the basic functionality for the gameplay 
# For example: shuffling a deck, distributing cards...

import random

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


class Player:

    def __init__(self, money):
        self.hand = []
        self.money = money #TODO

    def new_hand(self):
        self.hand = []

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

    def hit(self, card):
        self.hand.append(card)

    def split():
        # If same value split the hand into two possible hands
        return
    
    def double(self, card):
        # Double the money and take one card and stay

        #TODO add doubling money part and error checl

        self.hit(card)
        
    
    def surrender():
        # give up half a bet and retire from the game
        return
    

    # If stay then we just stop, no function necessary



class Game:

    def __init__(self):
        #TODO MONEY,100
        self.deck = Deck()
        self.deck.shuffle()

        self.house = Player(100)
        self.bot1 = Player(100)
        self.bot2 = Player(100)
        self.bot3 = Player(100)
        self.player = Player(100)

    def deal_initial_hands(self):
        self.cards_left_check()

        # Each player gets 2 cards
        for _ in range(2):
            self.house.hit(self.deck.deal_card())
            self.bot1.hit(self.deck.deal_card())
            self.bot2.hit(self.deck.deal_card())
            self.bot3.hit(self.deck.deal_card())
            self.player.hit(self.deck.deal_card())
    
    def cards_left_check(self):
        # 20 is a random number since 5 players if each plan to get 5 cards
        if len(self.deck.cards) <= 25:
            # Recreate the deck
            self.deck = Deck
            self.deck.shuffle()
        
    def deal_single_card(self, player_name):
        self.cards_left_check()

        if player_name == "house":
            self.house.hit(self.deck.deal_card())
        
        elif player_name == "bot1":
            self.bot1.hit(self.deck.deal_card())

        elif player_name == "bot2":
            self.bot2.hit(self.deck.deal_card())

        elif player_name == "bot3":
            self.bot3.hit(self.deck.deal_card())

        elif player_name == "player":
            self.player.hit(self.deck.deal_card())
