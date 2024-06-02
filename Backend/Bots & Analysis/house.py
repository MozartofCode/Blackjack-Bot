# 
#
# House stays on 17
# House hits if less than 17
# Matches bets

class House:

    def __init__(self, money):
        self.money = money
        self.hand = []
        
    def init_hand(self):
        self.hand = []

    def hit(self, card):
        self.hand.append(card)
        
    def stand(self):
        return
    
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

    def lose_money(self, loss):
        self.money -= loss
    
    def gain_money(self, gain):
        self.money += gain