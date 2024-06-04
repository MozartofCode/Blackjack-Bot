# @File: Basic Strategy.py
# @Author: Bertan Berker
# This is the algorithm that replicates the Basic Strategy in blackjack


# Basic strategy replicate that return the best possible move for a player
# :param house: the house, hand[0] is the faceup card for house
# :param player: player class
# :return: S (stand), H (hit), SP (split), Double (D), SU (surrender)
def apply_basic_strategy(house, player):
    
    value = player.calculate_hand_val()
    player_hand = []
    player_hand.append(player.hand[0].split(" of ")[0])
    player_hand.append(player.hand[1].split(" of ")[0])
    house_faceup = house.hand[0].split(" of ")[0]

    # Fixing/Adjusting the Syntax of Ace
    if house_faceup == "Ace":
        house_faceup = "A"

    if player_hand[0] == "Ace":
        player_hand[0] = "A"
    
    if player_hand[1] == "Ace":
        player_hand[1] = "A"
    

    if house_faceup == "2":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"



    elif house_faceup == "3":

        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "4":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "S"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "5":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "SP"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "S"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "6":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "SP"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "S"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "7":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "S"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "H"
        
        elif value == 16:
            return "H"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "8":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "H"
        
        elif value == 16:
            return "H"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "9":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "H"
        
        elif value == 16:
            return "SU"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup in ["10", "Jack", "Queen", "King"]:
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "H"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "S"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "H"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "SU"
        
        elif value == 16:
            return "SU"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "A":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "H"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SU"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "S"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "H"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "SU"
        
        elif value == 16:
            return "SU"
        
        elif value == 17:
            return "SU"

        elif value >= 18 and value <= 21:
            return "S"


# Basic strategy replicate that return the best possible move for a player's
# Second hand after they split
# :param house: the house, hand[0] is the faceup card for house
# :param player: player class
# :return: S (stand), H (hit), SP (split), Double (D), SU (surrender)
def apply_basic_strategy_2(house, player):
    
    value = player.calculate_hand_val_2()
    player_hand = []
    player_hand.append(player.hand2[0].split(" of ")[0])
    player_hand.append(player.hand2[1].split(" of ")[0])
    house_faceup = house.hand[0].split(" of ")[0]

    
    # Fixing/Adjusting the Syntax of Ace
    if house_faceup == "Ace":
        house_faceup = "A"

    if player_hand[0] == "Ace":
        player_hand[0] = "A"
    
    if player_hand[1] == "Ace":
        player_hand[1] = "A"
        

    if house_faceup == "2":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"



    elif house_faceup == "3":

        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "4":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "S"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "5":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "SP"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "S"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "6":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "SP"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "SP"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "D"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "D"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "D"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "S"
        
        elif value == 13 or value == 14:
            return "S"
        
        elif value == 15:
            return "S"
        
        elif value == 16:
            return "S"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "7":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "SP"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "SP"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "S"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "H"
        
        elif value == 16:
            return "H"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "8":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "H"
        
        elif value == 16:
            return "H"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "9":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "D"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "SP"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "D"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "H"
        
        elif value == 16:
            return "SU"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup in ["10", "Jack", "Queen", "King"]:
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "H"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SP"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "S"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "H"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "SU"
        
        elif value == 16:
            return "SU"
        
        elif value == 17:
            return "S"

        elif value >= 18 and value <= 21:
            return "S"

    
    elif house_faceup == "A":
        
        # PAIRS
        if (player_hand[0] == "2" and player_hand[1] == "2") or  (player_hand[0] == "3" and player_hand[1] == "3"):
            return "H"
        
        elif player_hand[0] == "4" and player_hand[1] == "4":
            return "H"
        
        elif player_hand[0] == "5" and player_hand[1] == "5":
            return "H"
        
        elif player_hand[0] == "6" and player_hand[1] == "6":
            return "H"
        
        elif player_hand[0] == "7" and player_hand[1] == "7":
            return "H"
        
        elif player_hand[0] == "8" and player_hand[1] == "8":
            return "SU"
        
        elif player_hand[0] == "9" and player_hand[1] == "9":
            return "S"
        
        elif player_hand[0] == "10" and player_hand[1] == "10":
            return "S"

        elif player_hand[0] == "A" and player_hand[1] == "A":
            return "SP"

        # SOFT TOTALS
        elif (player_hand[0] == "A" and player_hand[1] == "2" ) or  (player_hand[0] == "A" and player_hand[1] == "3") or \
            (player_hand[0] == "2" and player_hand[1] == "A") or  (player_hand[0] == "3" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "4" ) or  (player_hand[0] == "A" and player_hand[1] == "5") or \
            (player_hand[0] == "4" and player_hand[1] == "A") or  (player_hand[0] == "5" and player_hand[1] == "A"):
            return "H"

        elif (player_hand[0] == "A" and player_hand[1] == "6") or (player_hand[0] == "6" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "7") or (player_hand[0] == "7" and player_hand[1] == "A"):
            return "H"
        
        elif (player_hand[0] == "A" and player_hand[1] == "8") or (player_hand[0] == "8" and player_hand[1] == "A"):
            return "S"
        
        elif (player_hand[0] == "A" and player_hand[1] == "9") or (player_hand[0] == "9" and player_hand[1] == "A"):
            return "S"
        
        # HARD TOTALS (EXCLUDING PAIRS)
        elif value <= 8 and value >= 5:
            return "H"
        
        elif value == 9:
            return "H"
        
        elif value == 10:
            return "H"
        
        elif value == 11:
            return "D"
        
        elif value == 12:
            return "H"
        
        elif value == 13 or value == 14:
            return "H"
        
        elif value == 15:
            return "SU"
        
        elif value == 16:
            return "SU"
        
        elif value == 17:
            return "SU"

        elif value >= 18 and value <= 21:
            return "S"












