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
    print("Bot1 played...")

    move = bot1.play(house, bot1, True)
    bot1_playing = True
    
    # For split functionality
    bot1_playing_1 = True
    bot1_playing_2 = True

    if bot1.is_21():
        print("Blackjack!")
        bot1_playing = False
        bot1.gain_money(3 * bet // 2)
        house.lose_money(3 * bet // 2)

    elif move == "H":
        
        game.deal_single_card("bot1")

        while not bot1.is_over_21() and bot1.play(house, bot1, False) == "H":
            game.deal_single_card("bot1")

        if bot1.is_over_21():
            bot1.lose_money(bet)
            house.gain_money(bet)
            bot1_playing = False

    elif move == "S":
        bot1.stand()    
            
    elif move == "SU":
        bot1.surrender(bet)
        house.gain_money(bet//2)
        bot1_playing = False
            

    elif move == "SP":
        if bot1.money >= bet:
            

            # Two separate hands
            bot1.hand2.append(bot1.hand[-1])
            bot1.hand.pop()

            # For Hand1:
            game.deal_single_card("bot1")
            
                    
            if bot1.is_21():
                
                print("Blackjack!")
                bot1_playing_1 = False
                bot1.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)

            else:

                while not bot1.is_over_21() and bot1.play(house, bot1, False) == "H":
                    game.deal_single_card("bot1")

                if bot1.is_over_21():
                    bot1.lose_money(bet)
                    house.gain_money(bet)
                    bot1_playing_1 = False

            # For Hand2:
            game.deal_single_card_2("bot1")
            
            if bot1.calculate_hand_val_2() == 21:
                
                print("Blackjack!")
                bot1_playing_2 = False
                bot1.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)
            
            else:
                
                while bot1.calculate_hand_val_2() < 21 and bot1.play_2(house, bot1, False) == "H":
                    game.deal_single_card_2("bot1")

                if bot1.calculate_hand_val_2() > 21:
                    bot1.lose_money(bet)
                    house.gain_money(bet)
                    bot1_playing_2 = False



    elif move == "D":

        if bot1.money >= bet:
            game.deal_single_card("bot1")
            bet += bet

            print("Done")

            if bot1.is_over_21():
                bot1.lose_money(bet)
                house.gain_money(bet)
                bot1_playing = False
        else:
            bot1.hit(game.deal_single_card("bot1"))

            while not bot1.is_over_21() and bot1.play(house, bot1, False) == "H":
                bot1.hit(game.deal_single_card("bot1"))

            if bot1.is_over_21():
                bot1.lose_money(bet)
                bot1_playing = False

    
    if move != "SP":
        print(str(bot1.hand))

    else:

        if not bot1_playing_1 and not bot1_playing_2:
            bot1_playing = False

        print(str(bot1.hand))
        print(str(bot1.hand2))

        


    print()

    # print("Bot2 playing....")
    # #TODO: BOT2 play
    # print()

    # print("Bot3 playing....")
    # #TODO: BOT3 play
    # print()

    print("House played...")
    
    if move == "SP":

        if bot1_playing:

            if bot1_playing_1:
                
                while house.calculate_hand_val() < 17 and bot1.calculate_hand_val() > house.calculate_hand_val():
                    game.deal_single_card("house")
                
                if house.calculate_hand_val() > 21 or bot1.calculate_hand_val() > house.calculate_hand_val():
                    bot1.gain_money(bet)
                    house.lose_money(bet)
                
                elif house.calculate_hand_val() > bot1.calculate_hand_val():
                    bot1.lose_money(bet)
                    house.gain_money(bet)
                    

            if bot1_playing_2:
                
                while house.calculate_hand_val() < 17 and bot1.calculate_hand_val_2() > house.calculate_hand_val():
                    game.deal_single_card("house")
                
                if house.calculate_hand_val() > 21 or bot1.calculate_hand_val_2() > house.calculate_hand_val():
                    bot1.gain_money(bet)
                    house.lose_money(bet)
                
                elif house.calculate_hand_val() > bot1.calculate_hand_val_2():
                    bot1.lose_money(bet)
                    house.gain_money(bet)


    elif bot1_playing:

        while house.calculate_hand_val() < 17 and bot1.calculate_hand_val() > house.calculate_hand_val():
            game.deal_single_card("house")
        
        if house.calculate_hand_val() > 21 or bot1.calculate_hand_val() > house.calculate_hand_val():
            bot1.gain_money(bet)
            house.lose_money(bet)
        
        elif house.calculate_hand_val() > bot1.calculate_hand_val():
            bot1.lose_money(bet)
            house.gain_money(bet)
        

    
    print(str(house.hand))

    print()
    print_player_money(house, bot1, bot2, bot3)        

    


    






if __name__ == "__main__":
    main()