# @Author: Bertan Berker 
# @File: House.py
# House is the type of bot that simply hits if card values are
# less than 17 and stays on ar above 17 while matching players bets

class House:

    # Initializes the House class with a specified amount of money
    # :param money: the amount of money that house has
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.the_bet = 0
    

    # This is used for initializing or clearing the hand of the house
    # At the beginning of each play     
    def init_hand(self):
        self.hand = []

    def bet(self, the_bet):
        self.the_bet = the_bet
        self.money -= the_bet


    # ONLY USED FOR FULLSTACK PLAYER VS BOT

    def play(self, player, game):
        if player.calculate_hand_val() > 21:
            self.money += (self.the_bet * 2)
        
        elif player.calculate_hand_val() == 21:
            player.money += ((self.the_bet * 3) // 2)
            self.money -= (self.the_bet // 2)
        
        else:
            if self.calculate_hand_val() > player.calculate_hand_val():
                self.money += (self.the_bet * 2)
            
            elif self.calculate_hand_val() == player.calculate_hand_val():
                self.money += self.the_bet
                player.money += self.the_bet
            
            else:
                while self.calculate_hand_val() < 17 and self.calculate_hand_val() < player.calculate_hand_val():
                    self.hit(game.deal_single_card("house"))

                if self.calculate_hand_val() > 21 or self.calculate_hand_val() < player.calculate_hand_val():
                    player.money += (self.the_bet * 2)
                
                elif self.calculate_hand_val() == player.calculate_hand_val():
                    self.money += self.the_bet
                    player.money += self.the_bet
                
                elif self.calculate_hand_val() > player.calculate_hand_val():
                    self.money += (self.the_bet * 2)
                




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


    # Takes money from houses account (player won)
    # :param loss: House's loss 
    def lose_money(self, loss):
        self.money -= loss
    

    # Give money to House (player lost)
    # :param gain: money gained from other player
    def gain_money(self, gain):
        self.money += gain