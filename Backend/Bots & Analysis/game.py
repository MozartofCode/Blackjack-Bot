# This is a basic command line version of the frontend for further analysis of the performance of the bots

from gameplay import Game

def print_player_money(house, bot1, bot2, bot3):
    print("Each players money:")
    print("House: " + str(house.money))
    print("Bot1: " + str(bot1.money))
    print("Bot2: " + str(bot2.money))
    print("Bot3: " + str(bot3.money))
    

def print_player_cards(house, bot1, bot2, bot3):
    print("House: " + str(house.hand))
    print("Bot1: " + str(bot1.hand))
    print("Bot2: " + str(bot2.hand))
    print("Bot3: " + str(bot3.hand))

def print_initial_cards(house, bot1, bot2, bot3):
    print("House: " + str(house.hand[0]))
    print("Bot1: " + str(bot1.hand))
    print("Bot2: " + str(bot2.hand))
    print("Bot3: " + str(bot3.hand))


def main():

    game = Game()
    house = game.house
    bot1 = game.bot1
    bot2 = game.bot2
    bot3 = game.bot3

    print("Welcome to Casino Royale...")
    print("Let's play some blackjack!")
    print()

    print_player_money(house, bot1, bot2, bot3)

    # Betting
    
    print()
    print("Bot1 betting....")
    bet = bot1.bet(game)
    print("Bot1: $" + str(bet))

    print()
    print("Bot2 betting...")

    print()
    print("Bot3 betting...")

    # Dealing Cards

    print()
    print("Dealing cards...")
    game.deal_initial_hands()
    print_initial_cards(house, bot1, bot2, bot3)

    print()
    print("Bot1 playing...")

    move = bot1.play(house.hand, bot1.bot.hand, True)
    bot1_playing = True


    if move == "H":
        
        bot1.hit(game.deal_single_card("bot1"))

        while not bot1.is_over_21() and bot1.play(house.hand, bot1.bot.hand, False) == "H":
            bot1.hit(game.deal_single_card("bot1"))

        if bot1.is_over_21():
            bot1.lose_money(bet)
            bot1_playing = False

    elif move == "S":
        bot1.stand()    
            
    elif move == "SU":
        bot1.surrender(bet)
        bot1_playing = False
            
    #TODO
    elif move == "SP":
        if bot1.money >= bet:
            bot1.split(game.deal_single_card("bot1"))
            bet += bet
    #TODO   
    elif move == "D":
        if bot1.money >= bet:
            bot1.double(game.deal_single_card("bot1"))
            bet += bet

            if bot1.is_over_21():
                bot1.lose_money(bet)
                bot1_playing = False
        else:
            bot1.hit(game.deal_single_card("bot1"))

            while not bot1.is_over_21() and bot1.play(house.hand, bot1.bot.hand, False) == "H":
                bot1.hit(game.deal_single_card("bot1"))

            if bot1.is_over_21():
                bot1.lose_money(bet)
                bot1_playing = False

    
        
        


    print()

    # print("Bot2 playing....")
    # #TODO: BOT2 play
    # print()

    # print("Bot3 playing....")
    # #TODO: BOT3 play
    # print()

    print("House playing...")
    
    if bot1_playing:
        while house.calculate_hand_val() < 17:
            house.hit(game.deal_single_card("house"))
        
        if house.calculate_hand_val > 21 or bot1.calculate_hand_val() > house.calculate_hand_val():
            bot1.gain_money(bet)
            house.lose_money(bet)
        
        else:
            bot1.lose_money(bet)
            house.gain_money(bet)
        

        

    


    






if __name__ == "__main__":
    main()