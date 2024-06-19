# @Author: Bertan Berker
# @File: gameplay.py 
# This file contains the basic functionality for the gameplay 
# For example: shuffling a deck, distributing cards...

import random
from Bots.House import House
from Bots.Player import Player
from Bots.Bots.Bot1 import Bot1 
from Bots.Bots.Bot2 import Bot2
from Bots.Bots.Bot3 import Bot3
from Bots.Bots.Bot4 import Bot4
from Bots.Bots.Bot5 import Bot5
from Bots.Bots.Bot6 import Bot6

class Deck:

    # Initializing 5 decks of cards (5 x 52 cards)
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for i in range(5):        
            for suit in suits:
                for rank in ranks:
                    self.cards.append(rank + ' of ' + suit)


    # Shuffling the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)
    

    # Dealing one card from the deck
    # :return: the card or None if not possible
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    

    # Peeks but doesn't pops the card on top of deck
    # Used only with the card counting algorithm
    # :return: the card or None if not possible
    def peek_card(self): 
        
        if len(self.cards) > 0:
            return self.cards[-1]
        return None


class Game:

    # Initializes the players, money and deck for the game
    def __init__(self):
        house_money = 1000000
        player_money = 10000

        self.deck = Deck()
        self.deck.shuffle()
        self.card_count = 0     # For card counting purposes
        self.table_money = 0

        self.house = House(house_money)
        self.player = Player(player_money)
        self.bot1 = Bot1(player_money)
        self.bot2 = Bot2(player_money)
        self.bot3 = Bot3(player_money)
        self.bot4 = Bot4(player_money)
        self.bot5 = Bot5(player_money)
        self.bot6 = Bot6(player_money)
        

    # Clears players hands (used at the start of each play)
    def clear_hands(self):
        self.table_money = 0
        self.house.hand = []
        self.player.hand = []
        self.player.hand2 = []
        self.bot1.hand = []
        self.bot1.hand2 = []
        self.bot2.hand = []
        self.bot2.hand2 = []
        self.bot3.hand = []
        self.bot3.hand2 = []
        self.bot4.hand = []
        self.bot4.hand2 = []
        self.bot5.hand = []
        self.bot5.hand2 = []
        self.bot6.hand = []

    # Checks if enough cards are left in the deck and shuffles if not
    # 40 minimum is a random number since 8 players if each plan to get 5 cards
    def cards_left_check(self):
        if len(self.deck.cards) <= 40:
            self.deck = Deck()
            self.deck.shuffle()
            self.card_count = 0
        

    # Deals the initial hands to players
    # Each players gets 2 cards
    def deal_initial_hands(self, bot1_in_game, bot2_in_game, bot3_in_game, bot4_in_game, bot5_in_game, bot6_in_game):
        self.cards_left_check()

        for _ in range(2):
            self.house.hit(self.deck.deal_card())
            self.player.hit(self.deck.deal_card())
            
            if bot1_in_game:
                self.bot1.hit(self.deck.deal_card())
            
            if bot2_in_game:
                self.bot2.hit(self.deck.deal_card())
            
            if bot3_in_game:
                self.bot3.hit(self.deck.deal_card())
            
            if bot4_in_game:
                self.bot4.hit(self.deck.deal_card())
            
            if bot5_in_game:
                self.bot5.hit(self.deck.deal_card())
            
            if bot6_in_game:
                self.bot6.hit(self.deck.deal_card())
            
    

    # Deals a single card to a specific player (Hit)
    # :param player_name: name of the player to give the card to
    def deal_single_card(self, player_name):
        self.cards_left_check()
        self.card_count += self.count_card(self.deck.peek_card())

        if player_name == "house":
            self.house.hit(self.deck.deal_card())

        elif player_name == "player":
            self.player.hit(self.deck.deal_card())
        
        elif player_name == "bot1":
            self.bot1.hit(self.deck.deal_card())

        elif player_name == "bot2":
            self.bot2.hit(self.deck.deal_card())

        elif player_name == "bot3":
            self.bot3.hit(self.deck.deal_card())
        
        elif player_name == "bot4":
            self.bot4.hit(self.deck.deal_card())
        
        elif player_name == "bot5":
            self.bot5.hit(self.deck.deal_card())
        
        elif player_name == "bot6":
            self.bot6.hit(self.deck.deal_card())
    
    
    # Same as the deal single card for the second hand when a player splits
    # :param player_name: name of the player to give the card to
    def deal_single_card_2(self, player_name):
        self.cards_left_check()
        self.card_count += self.count_card(self.deck.peek_card())

        if player_name == "player":
            self.player.hit_2(self.deck.deal_card())
        
        elif player_name == "bot1":
            self.bot1.hit_2(self.deck.deal_card())
            
        elif player_name == "bot2":
            self.bot2.hit_2(self.deck.deal_card())

        elif player_name == "bot3":
            self.bot3.hit_2(self.deck.deal_card())
        
        elif player_name == "bot4":
            self.bot4.hit_2(self.deck.deal_card())
        
        elif player_name == "bot5":
            self.bot5.hit_2(self.deck.deal_card())


    # Hi - Lo Card Counting logic
    # 2-6 is +1
    # 7-9 is 0
    # 10-A is -1
    # :param card: the card that was dealt
    # :return: card count 
    def count_card(self, card):
        
        if card.split(" of ")[0] in ["Jack", "Queen", "King", "Ace"]:
            return -1
        elif card.split(" of ")[0] in ["7", "8", "9"]:
            return 0
        else:
            return 1