# @ Author: Bertan Berker
# @ Filename: gameplay_full.py
# This file has the gameplay fnuctions for the decentralized full-stack application

import random
from .smart_contract import Smart_Contract


class Player:

    # Initializes the Player class with a specified amount of money
    # :param money: the amount of money that player has
    # hand is the main hand while hand2 is only used as a result of splitting
    def __init__(self, contract):
        self.contract = contract
        self.hand = []
        self.in_game = True


    # Hit move in blackjack, adds a card to the player's hand
    # :param card: card to add
    def hit(self, card):
        self.hand.append(card)
    

    # Stand move in blackjack
    def stand(self):
        return
        
    
    # This function is used for calculating the value of player's hand
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
    
    
    # Checks if the value of player's hand is over 21 in which case it loses
    def is_over_21(self):
        if self.calculate_hand_val() > 21:
            return True
        return False                


    # Checks if the value of player's hand is 21 in which case it's blackjack
    def is_21(self):
        return self.calculate_hand_val() == 21


class House:

    # Initializes the House class with a specified amount of money
    # :param money: the amount of money that house has
    def __init__(self, contract):
        self.contract = contract
        self.hand = []
        self.in_game = True
    

    def play(self, game):

        if game.player.calculate_hand_val() > 21:            
            self.contract.add_to_house(self.contract.get_bet())
            self.contract.sub_from_player(self.contract.get_bet())
        
        elif game.player.calculate_hand_val() == 21:
            self.contract.add_to_player((self.contract.get_bet() * 3) // 2)
            self.contract.sub_from_house((self.contract.get_bet() * 3) // 2)
        
        else:
            if game.house.calculate_hand_val() > game.player.calculate_hand_val():    
                self.contract.add_to_house(self.contract.get_bet())
                self.contract.sub_from_player(self.contract.get_bet())
            
            elif game.house.calculate_hand_val() == game.player.calculate_hand_val():
                self.contract.add_to_house(0)
                self.contract.add_to_player(0)
            
            else:
                while game.house.calculate_hand_val() < 17 and game.house.calculate_hand_val() < game.player.calculate_hand_val():
                    game.deal_single_card("house") 

                if game.house.calculate_hand_val() > 21 or game.house.calculate_hand_val() < game.player.calculate_hand_val():        
                    self.contract.sub_from_house(self.contract.get_bet())
                    self.contract.add_to_player(self.contract.get_bet())
                
                elif game.house.calculate_hand_val() == game.player.calculate_hand_val():
                    self.contract.add_to_house(0)
                    self.contract.add_to_player(0)
                
                elif game.house.calculate_hand_val() > game.player.calculate_hand_val():
                    self.contract.add_to_house(self.contract.get_bet())
                    self.contract.sub_from_player(self.contract.get_bet())
                    


    # Hit move in blackjack, adds a card to the House's hand
    # :param card: card to add
    def hit(self, card):
        self.hand.append(card)
    

    # Stand move in blackjack
    def stand(self):
        return
    

    # This function is used for calculating the value of House's hand
    def calculate_hand_val(self):
        value = 0
        aces = 0

        for card in self.hand:
            val = card.split(" of ")[0]

            if val in ["Jack", "Queen", "King"]:
                value += 10
            
            # Add aces at the end for the proper value calculation
            elif val == "Ace":
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
    

    # Checks if the value of House's hand is over 21 in which case it loses
    def is_over_21(self):
        if self.calculate_hand_val() > 21:
            return True
        return False                


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

        self.contract = Smart_Contract()
        
        if (self.contract.get_player_balance() <= 0):
            self.contract.add_to_player(10000)

        self.deck = Deck()
        self.deck.shuffle()
        
        self.house = House(self.contract)
        self.player = Player(self.contract)

    # Checks if enough cards are left in the deck and shuffles if not
    # 40 minimum is a random number since 8 players if each plan to get 5 cards
    def cards_left_check(self):
        if len(self.deck.cards) <= 40:
            self.deck = Deck()
            self.deck.shuffle()
            self.card_count = 0
        

    # Deals the initial hands to players
    # Each players gets 2 cards
    def deal_initial_hands(self):
        self.cards_left_check()

        for _ in range(2):
            self.house.hit(self.deck.deal_card())
            self.player.hit(self.deck.deal_card())
            

    # Deals a single card to a specific player (Hit)
    # :param player_name: name of the player to give the card to
    def deal_single_card(self, player_name):
        self.cards_left_check()

        if player_name == "house":
            self.house.hit(self.deck.deal_card())

        elif player_name == "player":
            self.player.hit(self.deck.deal_card())
        
    
    def to_dict(self):
        return {
            'house': {
                'money': self.contract.get_house_balance(),
                'cards': [str(card) for card in self.house.hand],
                'bet': self.contract.get_bet(),
                'player_in_game': self.player.in_game,
                'house_in_game': self.house.in_game,
            },
            'player': {
                'money': self.contract.get_player_balance(),
                'bet': self.contract.get_bet(),
                'cards': [str(card) for card in self.player.hand],
                'player_in_game': self.player.in_game
            }
        }
