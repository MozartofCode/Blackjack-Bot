# @Author: Bertan Berker
# @File: Player.py
# This class allows me to play against the house in the simulation
# Most of the functionality is based on getting user input in the game so not many functions

class Player:

    # Initializes the Player class with a specified amount of money
    # :param money: the amount of money that player has
    # hand is the main hand while hand2 is only used as a result of splitting
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.hand2 = []
        self.the_bet = 0
        self.in_game = True


    # Hit move in blackjack, adds a card to the player's hand
    # :param card: card to add
    def hit(self, card):
        self.hand.append(card)
    
    
    # Same as Hit move but for adding a card to the player's hand2 (after split)
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
    
    
    # This function is used for calculating the value of player's hand2 (after splitting)
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
    

    # Checks if the value of player's hand is over 21 in which case it loses
    def is_over_21(self):
        if self.calculate_hand_val() > 21:
            return True
        return False                


    # Checks if the value of player's hand is 21 in which case it's blackjack
    def is_21(self):
        return self.calculate_hand_val() == 21


    # Takes money from player's account (house won)
    # :param loss: House's loss 
    def lose_money(self, loss):
        self.money -= loss
    

    # Give money to player (house lost)
    # :param gain: money gained from other player
    def gain_money(self, gain):
        self.money += gain