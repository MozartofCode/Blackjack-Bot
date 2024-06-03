# AI-powered bot (pretrained bot from hugging face...)

class Bot2:
    def __init__(self, money):
        self.money = money
        self.hand = []

    
    def hit(self, card):
        self.hand.append(card)
        
    def calculate_hand_val(self):
        return    
    