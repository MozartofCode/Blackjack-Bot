# @Author: Bertan Berker
# @File: game.py
# This is a basic command line version of the game of blackjack where bots are playing against each other
# And this program aims to compare their performances

from gameplay import Game
import csv

# This function is used for generating data for the csv that will be used by bot2 (NN)
# :param data_row: one row of data to be added to the csv file 
# [player_hand, dealer_hand, count, move, bet]
def generate_csv_dataset(data_row):
    filename = "blackjack_dataset.csv"

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_row)


# This function creates the csv file that I'll populate later
# Adds the headers to the file
def create_csv_dataset():
    filename = 'blackjack_dataset.csv'
    headers = ['Player Hand', 'House Upcard', 'Count', 'Move', 'Bet']

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)


# This function prints how much money each player has
# :param house: the house
# :param bot1: bot1 player
# :param bot2: bot2 player
# :param bot3: bot3 player
def print_player_money(house, bot1, bot2, bot3):
    print("Each players money:")
    print("House: " + str(house.money))
    print("Bot1: " + str(bot1.money))
    print("Bot2: " + str(bot2.money))
    print("Bot3: " + str(bot3.money))
    

# This function prints each player's hands
# :param house: the house
# :param bot1: bot1 player
# :param bot2: bot2 player
# :param bot3: bot3 player
def print_player_cards(house, bot1, bot2, bot3):
    print("House: " + str(house.hand))
    print("Bot1: " + str(bot1.hand))
    print("Bot2: " + str(bot2.hand))
    print("Bot3: " + str(bot3.hand))


# This function specificially prints each player's initial hands (only one card is shown for house)
# :param house: the house
# :param bot1: bot1 player
# :param bot2: bot2 player
# :param bot3: bot3 player
def print_initial_cards(house, bot1, bot2, bot3):
    print("House: " + str(house.hand[0]))
    print("Bot1: " + str(bot1.hand))
    print("Bot2: " + str(bot2.hand))
    print("Bot3: " + str(bot3.hand))


# This function calculates the percentage of loss or profit for a player 
# After the simulation is over
# :param init_money: Initial amount of money I player had
# :param final_money: Final amount of money I player has
# :return: the percentage of loss or profit
def calculate_profit_loss_percentage(init_money, final_money):
    return round(((final_money - init_money)/init_money) * 100, 2)


# This is the main function that runs the simulation (game)
# Simulation and the Analysis is going to be based on 1000 played hands
def main():
    game_count = 10
    game = Game()
    
    #create_csv_dataset()
    
    print("Welcome to Casino Royale...")
    print("Let's play some blackjack!")
    print()
    
    while game_count > 0:
        
        game.clear_hands()
        game_count -= 1

        house = game.house
        bot1 = game.bot1
        bot2 = game.bot2
        bot3 = game.bot3

        if bot1.money <= 0:
            
            print()
            print("Game Over for Bot1...")
            break

        elif house.money <= 0:
            print("Game Over for House...")
            break
        
        print("Let's play a new hand...")
        print()

        print_player_money(house, bot1, bot2, bot3)

        # Betting
        
        print()
        print("Bot1 betting....")
        bet = bot1.bet(game)
        print("Bot1: $" + str(bet))

        print()
        print("Bot2 betting...")        
        bot2_bet = bot2.bet(game)
        print("Bot2: $" + str(bet))

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

        # Adding the play to the csv file
        # data_row = [list(bot1.hand), house.hand[0], game.card_count, move, bet]
        # generate_csv_dataset(data_row)

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
        print("Bot2 played...")

        bot2_move = bot2.play(bot2.hand, house.hand[0], game.card_count, bot2_bet, True)
        bot2_playing = True
        
        print(bot2_move)

        # For split functionality
        bot2_playing_1 = True
        bot2_playing_2 = True

        if bot2.is_21():
            print("Blackjack!")
            bot2_playing = False
            bot2.gain_money(3 * bet // 2)
            house.lose_money(3 * bet // 2)

        elif bot2_move == "H":
            
            game.deal_single_card("bot2")

            while not bot2.is_over_21() and bot2.play(bot2.hand, house.hand[0], game.card_count, bot2_bet, False) == "H":
                game.deal_single_card("bot2")

            if bot2.is_over_21():
                bot2.lose_money(bet)
                house.gain_money(bet)
                bot2_playing = False

        elif bot2_move == "S":
            bot2.stand()    
                
        elif bot2_move == "SU":
            bot2.surrender(bet)
            house.gain_money(bet//2)
            bot2_playing = False
                

        elif bot2_move == "SP":
            if bot2.money >= bet:
                
                # Two separate hands
                bot2.hand2.append(bot2.hand[-1])
                bot2.hand.pop()

                # For Hand1:
                game.deal_single_card("bot2")
                
                        
                if bot2.is_21():
                    
                    print("Blackjack!")
                    bot1_playing_2 = False
                    bot2.gain_money(3 * bet // 2)
                    house.lose_money(3 * bet // 2)

                else:

                    while not bot2.is_over_21() and bot2.play(bot2.hand, house.hand[0], game.card_count, bot2_bet, False) == "H":
                        game.deal_single_card("bot2")

                    if bot2.is_over_21():
                        bot2.lose_money(bet)
                        house.gain_money(bet)
                        bot2_playing_1 = False

                # For Hand2:
                game.deal_single_card_2("bot2")
                
                if bot2.calculate_hand_val_2() == 21:
                    
                    print("Blackjack!")
                    bot2_playing_2 = False
                    bot2.gain_money(3 * bet // 2)
                    house.lose_money(3 * bet // 2)
                
                else:
                    
                    while bot2.calculate_hand_val_2() < 21 and bot2.play_2(bot2.hand2, house.hand[0], game.card_count, bot2_bet, False) == "H":
                        game.deal_single_card_2("bot2")

                    if bot2.calculate_hand_val_2() > 21:
                        bot2.lose_money(bet)
                        house.gain_money(bet)
                        bot2_playing_2 = False


        elif bot2_move == "D":

            if bot2.money >= bet:
                game.deal_single_card("bot2")
                bet += bet

                if bot2.is_over_21():
                    bot2.lose_money(bet)
                    house.gain_money(bet)
                    bot2_playing = False
            else:
                bot2.hit(game.deal_single_card("bot2"))

                while not bot2.is_over_21() and bot2.play(bot2.hand, house.hand[0], game.card_count, bot2_bet, False) == "H":
                    bot1.hit(game.deal_single_card("bot2"))

                if bot2.is_over_21():
                    bot2.lose_money(bet)
                    bot2_playing = False

        
        if move != "SP":
            print(str(bot2.hand))

        else:

            if not bot2_playing_1 and not bot2_playing_2:
                bot2_playing = False

            print(str(bot2.hand))
            print(str(bot2.hand2))



  

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

        if game_count == 0:
            print("Simulation finished after playing 1000 hands..." )
            print()
            print_player_money(house, bot1, bot2, bot3)    
            print()

            if bot1.money < 10000:
                print("Total loss of Bot1: " + str(calculate_profit_loss_percentage(10000, bot1.money)) + "%")

            else:
                print("Total profit of Bot1: " + str(calculate_profit_loss_percentage(10000, bot1.money)) + "%")

    
if __name__ == "__main__":
    main()