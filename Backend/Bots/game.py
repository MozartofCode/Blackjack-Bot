# @Author: Bertan Berker
# @File: game.py
# This is a basic command line version of the game of blackjack where bots are playing against each other
# And this program aims to compare their performances

from Bots.gameplay import Game
import csv

# This function is used for generating data for the csv that will be used by bot2 (NN)
# :param data_row: one row of data to be added to the csv file 
# [player_hand, dealer_hand, count, move, bet]
def generate_csv_dataset(dataset_name, data_row):
    filename = dataset_name

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_row)


# This function creates the csv file that I'll populate later
# Adds the headers to the file
def create_csv_dataset(dataset_name, headers):
    filename = dataset_name
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)


# This function prints how much money each player has
# :param house: the house
# :param bot1: bot1 player
# :param bot2: bot2 player
# :param bot3: bot3 player
def print_player_money(house, bot1, bot2, bot3, bot4, bot5, bot6):
    print("Each players money:")
    print("House: $" + str(house.money))
    print("Bot1: $" + str(bot1.money))
    print("Bot2: $" + str(bot2.money))
    print("Bot3: $" + str(bot3.money))
    print("Bot4: $" + str(bot4.money))
    print("Bot5: $" + str(bot5.money))
    print("Bot6: $" + str(bot6.money))
    

# This function prints each player's hands
# :param house: the house
# :param bot1: bot1 player
# :param bot2: bot2 player
# :param bot3: bot3 player
def print_player_cards(house, bot1, bot2, bot3, bot4, bot5, bot6):
    print("House: " + str(house.hand))
    print("Bot1: " + str(bot1.hand))
    print("Bot2: " + str(bot2.hand))
    print("Bot3: " + str(bot3.hand))
    print("Bot4: " + str(bot4.hand))
    print("Bot5: " + str(bot5.hand))
    print("Bot6: " + str(bot6.hand))
    

# This function specificially prints each player's initial hands (only one card is shown for house)
# :param house: the house
# :param bot1: bot1 player
# :param bot2: bot2 player
# :param bot3: bot3 player
def print_initial_cards(house, bot1, bot2, bot3, bot4, bot5, bot6):
    print("House: " + str(house.hand[0]))
    print("Bot1: " + str(bot1.hand))
    print("Bot2: " + str(bot2.hand))
    print("Bot3: " + str(bot3.hand))
    print("Bot4: " + str(bot4.hand))
    print("Bot5: " + str(bot5.hand))
    print("Bot6: " + str(bot6.hand))


# This function calculates the percentage of loss or profit for a player 
# After the simulation is over
# :param init_money: Initial amount of money I player had
# :param final_money: Final amount of money I player has
# :return: the percentage of loss or profit
def calculate_profit_loss_percentage(init_money, final_money):
    return round(((final_money - init_money)/init_money) * 100, 2)



def print_calculated_profits(house, bot1, bot2, bot3, bot4, bot5, bot6):
    if house.money < 1000000:
        print("Total loss of House: " + str(calculate_profit_loss_percentage(1000000, house.money)) + "%")
    else:
        print("Total profit of House: " + str(calculate_profit_loss_percentage(1000000, house.money)) + "%")

    if bot1.money < 10000:
        print("Total loss of Bot1: " + str(calculate_profit_loss_percentage(10000, bot1.money)) + "%")
    else:
        print("Total profit of Bot1: " + str(calculate_profit_loss_percentage(10000, bot1.money)) + "%")
    
    if bot2.money < 10000:
        print("Total loss of Bot2: " + str(calculate_profit_loss_percentage(10000, bot2.money)) + "%")
    else:
        print("Total profit of Bot2: " + str(calculate_profit_loss_percentage(10000, bot2.money)) + "%")
    
    if bot3.money < 10000:
        print("Total loss of Bot3: " + str(calculate_profit_loss_percentage(10000, bot3.money)) + "%")
    else:
        print("Total profit of Bot3: " + str(calculate_profit_loss_percentage(10000, bot3.money)) + "%")
    
    if bot4.money < 10000:
        print("Total loss of Bot4: " + str(calculate_profit_loss_percentage(10000, bot4.money)) + "%")
    else:
        print("Total profit of Bot4: " + str(calculate_profit_loss_percentage(10000, bot4.money)) + "%")
    
    if bot5.money < 10000:
        print("Total loss of Bot5: " + str(calculate_profit_loss_percentage(10000, bot5.money)) + "%")
    else:
        print("Total profit of Bot5: " + str(calculate_profit_loss_percentage(10000, bot5.money)) + "%")
    
    if bot6.money < 10000:
        print("Total loss of Bot6: " + str(calculate_profit_loss_percentage(10000, bot6.money)) + "%")
    else:
        print("Total profit of Bot6: " + str(calculate_profit_loss_percentage(10000, bot6.money)) + "%")
    


def bot1_playing(bot1, house, game, bet):
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
        
        while (not bot1.is_over_21() or not bot1.is_21) and bot1.play(house, bot1, False) == "H":
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
            game.deal_single_card_2("bot1")
                        
            if bot1.is_21():     
                print("Blackjack!")
                bot1_playing_1 = False
                bot1.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)

            else:
                while (not bot1.is_over_21() or not bot1.is_21) and bot1.play(house, bot1, False) == "H":
                    game.deal_single_card("bot1")

                if bot1.is_over_21():
                    bot1.lose_money(bet)
                    house.gain_money(bet)
                    bot1_playing_1 = False

            # For Hand2:
                
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

            if bot1.is_over_21():
                bot1.lose_money(bet)
                house.gain_money(bet)
                bot1_playing = False
        
    if move != "SP":
        print(str(bot1.hand))

    else:
        if not bot1_playing_1 and not bot1_playing_2:
            bot1_playing = False

        print(str(bot1.hand))
        print(str(bot1.hand2))
    
    return [bot1_playing_1, bot1_playing_2, bot1_playing, move, bet, bot1]
        


def bot2_playing(bot2, house, game, bet):
    bot2_move = bot2.play(bot2.hand, house.hand[0], game.card_count, bet, True)
    bot2_playing = True

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

        while (not bot2.is_over_21() or not bot2.is_21) and bot2.play(bot2.hand, house.hand[0], game.card_count, bet, False) == "H":
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
            game.deal_single_card_2("bot2")
                        
            if bot2.is_21():  
                print("Blackjack!")
                bot2_playing_2 = False
                bot2.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)

            else:
                while (not bot2.is_over_21() or not bot2.is_21) and bot2.play(bot2.hand, house.hand[0], game.card_count, bet, False) == "H":
                    game.deal_single_card("bot2")

                if bot2.is_over_21():
                    bot2.lose_money(bet)
                    house.gain_money(bet)
                    bot2_playing_1 = False

            # For Hand2:
                
            if bot2.calculate_hand_val_2() == 21:
                print("Blackjack!")
                bot2_playing_2 = False
                bot2.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)
                
            else: 
                while bot2.calculate_hand_val_2() < 21 and bot2.play_2(bot2.hand2, house.hand[0], game.card_count, bet, False) == "H":
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


    if bot2_move != "SP":
        print(str(bot2.hand))

    else:
        if not bot2_playing_1 and not bot2_playing_2:
            bot2_playing = False

        print(str(bot2.hand))
        print(str(bot2.hand2))
    
    return [bot2_playing_1, bot2_playing_2, bot2_playing, bot2_move, bet, bot2]



def bot3_playing(bot3, house, game, bet):
    bot3_move = bot3.play(bot3.hand, house.hand[0], game.card_count, bet, True)
    bot3_playing = True

    # For split functionality
    bot3_playing_1 = True
    bot3_playing_2 = True

    if bot3.is_21():
        print("Blackjack!")
        bot3_playing = False
        bot3.gain_money(3 * bet // 2)
        house.lose_money(3 * bet // 2)

    elif bot3_move == "H":
        game.deal_single_card("bot3")

        while (not bot3.is_over_21() or not bot3.is_21) and bot3.play(bot3.hand, house.hand[0], game.card_count, bet, False) == "H":
            game.deal_single_card("bot3")

        if bot3.is_over_21():
            bot3.lose_money(bet)
            house.gain_money(bet)
            bot3_playing = False

    elif bot3_move == "S":
        bot3.stand()    
                
    elif bot3_move == "SU":
        bot3.surrender(bet)
        house.gain_money(bet//2)
        bot3_playing = False
                

    elif bot3_move == "SP":
        if bot3.money >= bet: 
            # Two separate hands
            bot3.hand2.append(bot3.hand[-1])
            bot3.hand.pop()

            # For Hand1:
            game.deal_single_card("bot3")
            game.deal_single_card_2("bot3")
                        
            if bot3.is_21():  
                print("Blackjack!")
                bot3_playing_2 = False
                bot3.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)

            else:
                while (not bot3.is_over_21() or not bot3.is_21) and bot3.play(bot3.hand, house.hand[0], game.card_count, bet, False) == "H":
                    game.deal_single_card("bot3")

                if bot3.is_over_21():
                    bot3.lose_money(bet)
                    house.gain_money(bet)
                    bot3_playing_1 = False

            # For Hand2:
                
            if bot3.calculate_hand_val_2() == 21:
                print("Blackjack!")
                bot3_playing_2 = False
                bot3.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)
                
            else: 
                while bot3.calculate_hand_val_2() < 21 and bot3.play_2(bot3.hand2, house.hand[0], game.card_count, bet, False) == "H":
                    game.deal_single_card_2("bot3")

                if bot3.calculate_hand_val_2() > 21:
                    bot3.lose_money(bet)
                    house.gain_money(bet)
                    bot3_playing_2 = False

    elif bot3_move == "D":
        if bot3.money >= bet:
            game.deal_single_card("bot3")
            bet += bet

            if bot3.is_over_21():
                bot3.lose_money(bet)
                house.gain_money(bet)
                bot3_playing = False


    if bot3_move != "SP":
        print(str(bot3.hand))

    else:
        if not bot3_playing_1 and not bot3_playing_2:
            bot3_playing = False

        print(str(bot3.hand))
        print(str(bot3.hand2))
    
    return [bot3_playing_1, bot3_playing_2, bot3_playing, bot3_move, bet, bot3]



def bot4_playing(bot4, house, game, bet):
    bot4_move = bot4.play(bot4.hand, house.hand[0], game.card_count, bet, True)
    bot4_playing = True

    # For split functionality
    bot4_playing_1 = True
    bot4_playing_2 = True

    if bot4.is_21():
        print("Blackjack!")
        bot4_playing = False
        bot4.gain_money(3 * bet // 2)
        house.lose_money(3 * bet // 2)

    elif bot4_move == "H":
        game.deal_single_card("bot4")

        while (not bot4.is_over_21() or not bot4.is_21) and bot4.play(bot4.hand, house.hand[0], game.card_count, bet, False) == "H":
            game.deal_single_card("bot4")

        if bot4.is_over_21():
            bot4.lose_money(bet)
            house.gain_money(bet)
            bot4_playing = False

    elif bot4_move == "S":
        bot4.stand()    
                
    elif bot4_move == "SU":
        bot4.surrender(bet)
        house.gain_money(bet//2)
        bot4_playing = False
                

    elif bot4_move == "SP":
        if bot4.money >= bet: 
            # Two separate hands
            bot4.hand2.append(bot4.hand[-1])
            bot4.hand.pop()

            # For Hand1:
            game.deal_single_card("bot4")
            game.deal_single_card_2("bot4")
                        
            if bot4.is_21():  
                print("Blackjack!")
                bot4_playing_2 = False
                bot4.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)

            else:
                while (not bot4.is_over_21() or not bot4.is_21) and bot4.play(bot4.hand, house.hand[0], game.card_count, bet, False) == "H":
                    game.deal_single_card("bot4")

                if bot4.is_over_21():
                    bot4.lose_money(bet)
                    house.gain_money(bet)
                    bot4_playing_1 = False

            # For Hand2:
                
            if bot4.calculate_hand_val_2() == 21:
                print("Blackjack!")
                bot4_playing_2 = False
                bot4.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)
                
            else: 
                while bot4.calculate_hand_val_2() < 21 and bot4.play_2(bot4.hand2, house.hand[0], game.card_count, bet, False) == "H":
                    game.deal_single_card_2("bot4")

                if bot4.calculate_hand_val_2() > 21:
                    bot4.lose_money(bet)
                    house.gain_money(bet)
                    bot4_playing_2 = False

    elif bot4_move == "D":
        if bot4.money >= bet:
            game.deal_single_card("bot4")
            bet += bet

            if bot4.is_over_21():
                bot4.lose_money(bet)
                house.gain_money(bet)
                bot4_playing = False


    if bot4_move != "SP":
        print(str(bot4.hand))

    else:
        if not bot4_playing_1 and not bot4_playing_2:
            bot4_playing = False

        print(str(bot4.hand))
        print(str(bot4.hand2))
    
    return [bot4_playing_1, bot4_playing_2, bot4_playing, bot4_move, bet, bot4]


def bot5_playing(bot5, house, game, bet):
    
    bot5_move = bot5.play(bot5.hand, house.hand[0], game.card_count, bet, True)
    bot5_playing = True

    # For split functionality
    bot5_playing_1 = True
    bot5_playing_2 = True

    if bot5.is_21():
        print("Blackjack!")
        bot5_playing = False
        bot5.gain_money(3 * bet // 2)
        house.lose_money(3 * bet // 2)

    elif bot5_move == "H":
        game.deal_single_card("bot5")

        while (not bot5.is_over_21() or not bot5.is_21) and bot5.play(bot5.hand, house.hand[0], game.card_count, bet, False) == "H":
            game.deal_single_card("bot5")

        if bot5.is_over_21():
            bot5.lose_money(bet)
            house.gain_money(bet)
            bot5_playing = False

    elif bot5_move == "S":
        bot5.stand()    
                
    elif bot5_move == "SU":
        bot5.surrender(bet)
        house.gain_money(bet//2)
        bot5_playing = False
                

    elif bot5_move == "SP":
        if bot5.money >= bet: 
            # Two separate hands
            bot5.hand2.append(bot5.hand[-1])
            bot5.hand.pop()

            # For Hand1:
            game.deal_single_card("bot5")
            game.deal_single_card_2("bot5")
                        
            if bot5.is_21():  
                print("Blackjack!")
                bot5_playing_2 = False
                bot5.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)

            else:
                while (not bot5.is_over_21() or not bot5.is_21) and bot5.play(bot5.hand, house.hand[0], game.card_count, bet, False) == "H":
                    game.deal_single_card("bot5")

                if bot5.is_over_21():
                    bot5.lose_money(bet)
                    house.gain_money(bet)
                    bot5_playing_1 = False

            # For Hand2:
                
            if bot5.calculate_hand_val_2() == 21:
                print("Blackjack!")
                bot5_playing_2 = False
                bot5.gain_money(3 * bet // 2)
                house.lose_money(3 * bet // 2)
                
            else: 
                while bot5.calculate_hand_val_2() < 21 and bot5.play_2(bot5.hand2, house.hand[0], game.card_count, bet, False) == "H":
                    game.deal_single_card_2("bot5")

                if bot5.calculate_hand_val_2() > 21:
                    bot5.lose_money(bet)
                    house.gain_money(bet)
                    bot5_playing_2 = False

    elif bot5_move == "D":
        if bot5.money >= bet:
            game.deal_single_card("bot5")
            bet += bet

            if bot5.is_over_21():
                bot5.lose_money(bet)
                house.gain_money(bet)
                bot5_playing = False


    if bot5_move != "SP":
        print(str(bot5.hand))

    else:
        if not bot5_playing_1 and not bot5_playing_2:
            bot5_playing = False

        print(str(bot5.hand))
        print(str(bot5.hand2))
    
    return [bot5_playing_1, bot5_playing_2, bot5_playing, bot5_move, bet, bot5]



def bot6_playing(bot6, house, game, bet):
    bot6_move = bot6.play(bot6, house.hand[0])
    bot6_playing = True

    if bot6.is_21():
        print("Blackjack!")
        bot6_playing = False
        bot6.gain_money(3 * bet // 2)
        house.lose_money(3 * bet // 2)

    elif bot6_move == "H":
        game.deal_single_card("bot6")

        while (not bot6.is_over_21() or not bot6.is_21) and bot6.play(bot6, house.hand[0]) == "H":
            game.deal_single_card("bot6")

        if bot6.is_over_21():
            bot6.lose_money(bet)
            house.gain_money(bet)
            bot6_playing = False

    elif bot6_move == "S":
        bot6.stand()    
    
    print(str(bot6.hand))

    return [True, True, bot6_playing, bot6_move, bet, bot6]




# House starts by looking if there is any cards playing that it's immediately better before hitting and gets rid of them
# results = [bot2_playing_1, bot2_playing_2, bot2_playing, bot2_move, bot2_bet, bot2] etc.
def house_playing(game, house, bot1_results, bot2_results, bot3_results, bot4_results, bot5_results, bot6_results):
        
    # Looking at each hand initially for an easy win
    
    if bot1_results[3] == "SP":
        if bot1_results[2]:
            if bot1_results[0]:
                
                if house.calculate_hand_val() > bot1_results[5].calculate_hand_val():
                    bot1_results[5].lose_money(bot1_results[4])
                    house.gain_money(bot1_results[4])
                    bot1_results[0] = False

            if bot1_results[1]:
                if house.calculate_hand_val() > bot1_results[5].calculate_hand_val_2():
                    bot1_results[5].lose_money(bot1_results[4])
                    house.gain_money(bot1_results[4])
                    bot1_results[1] = False
    
    elif bot1_results[2]:
        if house.calculate_hand_val() > bot1_results[5].calculate_hand_val():
            bot1_results[5].lose_money(bot1_results[4])
            house.gain_money(bot1_results[4])
            bot1_results[2] = False


    if bot2_results[3] == "SP":
        if bot2_results[2]:
            if bot2_results[0]:
                
                if house.calculate_hand_val() > bot2_results[5].calculate_hand_val():
                    bot2_results[5].lose_money(bot2_results[4])
                    house.gain_money(bot2_results[4])
                    bot2_results[0] = False

            if bot2_results[1]:
                if house.calculate_hand_val() > bot2_results[5].calculate_hand_val_2():
                    bot2_results[5].lose_money(bot2_results[4])
                    house.gain_money(bot2_results[4])
                    bot2_results[1] = False
    
    elif bot2_results[2]:
        if house.calculate_hand_val() > bot2_results[5].calculate_hand_val():
            bot2_results[5].lose_money(bot2_results[4])
            house.gain_money(bot2_results[4])
            bot2_results[2] = False

    if bot3_results[3] == "SP":
        if bot3_results[2]:
            if bot3_results[0]:
                
                if house.calculate_hand_val() > bot3_results[5].calculate_hand_val():
                    bot3_results[5].lose_money(bot3_results[4])
                    house.gain_money(bot3_results[4])
                    bot3_results[0] = False

            if bot3_results[1]:
                if house.calculate_hand_val() > bot3_results[5].calculate_hand_val_2():
                    bot3_results[5].lose_money(bot3_results[4])
                    house.gain_money(bot3_results[4])
                    bot3_results[1] = False
    
    elif bot3_results[2]:
        if house.calculate_hand_val() > bot3_results[5].calculate_hand_val():
            bot3_results[5].lose_money(bot3_results[4])
            house.gain_money(bot3_results[4])
            bot3_results[2] = False

    if bot4_results[3] == "SP":
        if bot4_results[2]:
            if bot4_results[0]:
                
                if house.calculate_hand_val() > bot4_results[5].calculate_hand_val():
                    bot4_results[5].lose_money(bot4_results[4])
                    house.gain_money(bot4_results[4])
                    bot4_results[0] = False

            if bot4_results[1]:
                if house.calculate_hand_val() > bot4_results[5].calculate_hand_val_2():
                    bot4_results[5].lose_money(bot4_results[4])
                    house.gain_money(bot4_results[4])
                    bot4_results[1] = False
    
    elif bot4_results[2]:
        if house.calculate_hand_val() > bot4_results[5].calculate_hand_val():
            bot4_results[5].lose_money(bot4_results[4])
            house.gain_money(bot4_results[4])
            bot4_results[2] = False

    if bot5_results[3] == "SP":
        if bot5_results[2]:
            if bot5_results[0]:
                
                if house.calculate_hand_val() > bot5_results[5].calculate_hand_val():
                    bot5_results[5].lose_money(bot5_results[4])
                    house.gain_money(bot5_results[4])
                    bot5_results[0] = False

            if bot5_results[1]:
                if house.calculate_hand_val() > bot5_results[5].calculate_hand_val_2():
                    bot5_results[5].lose_money(bot5_results[4])
                    house.gain_money(bot5_results[4])
                    bot5_results[1] = False
    
    elif bot5_results[2]:
        if house.calculate_hand_val() > bot5_results[5].calculate_hand_val():
            bot5_results[5].lose_money(bot5_results[4])
            house.gain_money(bot5_results[4])
            bot5_results[2] = False

    if bot6_results[2]:
        if house.calculate_hand_val() > bot6_results[5].calculate_hand_val():
            bot6_results[5].lose_money(bot6_results[4])
            house.gain_money(bot6_results[4])
            bot6_results[2] = False
        

    # Now looking at each one specifically
    # Looking at bot 1
    if bot1_results[3] == "SP":
        if bot1_results[2]:
            if bot1_results[0]:
                while house.calculate_hand_val() < 17 and bot1_results[5].calculate_hand_val() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot1_results[5].calculate_hand_val() > house.calculate_hand_val():
                    bot1_results[5].gain_money(bot1_results[4])
                    house.lose_money(bot1_results[4])
                    
                elif house.calculate_hand_val() > bot1_results[5].calculate_hand_val():
                    bot1_results[5].lose_money(bot1_results[4])
                    house.gain_money(bot1_results[4])

            if bot1_results[1]:
                while house.calculate_hand_val() < 17 and bot1_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot1_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    bot1_results[5].gain_money(bot1_results[4])
                    house.lose_money(bot1_results[4])
                    
                elif house.calculate_hand_val() > bot1_results[5].calculate_hand_val_2():
                    bot1_results[5].lose_money(bot1_results[4])
                    house.gain_money(bot1_results[4])

        elif bot1_results[2]:
            while house.calculate_hand_val() < 17 and bot1_results[5].calculate_hand_val() > house.calculate_hand_val():
                game.deal_single_card("house")
            
            if house.calculate_hand_val() > 21 or bot1_results[5].calculate_hand_val() > house.calculate_hand_val():
                bot1_results[5].gain_money(bot1_results[4])
                house.lose_money(bot1_results[4])
            
            elif house.calculate_hand_val() > bot1_results[5].calculate_hand_val():
                bot1_results[5].lose_money(bot1_results[4])
                house.gain_money(bot1_results[4])

    elif bot1_results[2]:
        while house.calculate_hand_val() < 17 and bot1_results[5].calculate_hand_val() > house.calculate_hand_val():
            game.deal_single_card("house")
                    
        if house.calculate_hand_val() > 21 or bot1_results[5].calculate_hand_val() > house.calculate_hand_val():
            bot1_results[5].gain_money(bot1_results[4])
            house.lose_money(bot1_results[4])
                    
        elif house.calculate_hand_val() > bot1_results[5].calculate_hand_val():
            bot1_results[5].lose_money(bot1_results[4])
            house.gain_money(bot1_results[4])



    # Looking at bot 2
    if bot2_results[3] == "SP":
        if bot2_results[2]:
            if bot2_results[0]:
                while house.calculate_hand_val() < 17 and bot2_results[5].calculate_hand_val() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot2_results[5].calculate_hand_val() > house.calculate_hand_val():
                    bot2_results[5].gain_money(bot2_results[4])
                    house.lose_money(bot2_results[4])
                    
                elif house.calculate_hand_val() > bot2_results[5].calculate_hand_val():
                    bot2_results[5].lose_money(bot2_results[4])
                    house.gain_money(bot2_results[4])

            if bot2_results[1]:
                while house.calculate_hand_val() < 17 and bot2_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot2_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    bot2_results[5].gain_money(bot2_results[4])
                    house.lose_money(bot2_results[4])
                    
                elif house.calculate_hand_val() > bot2_results[5].calculate_hand_val_2():
                    bot2_results[5].lose_money(bot2_results[4])
                    house.gain_money(bot2_results[4])

        elif bot2_results[2]:
            while house.calculate_hand_val() < 17 and bot2_results[5].calculate_hand_val() > house.calculate_hand_val():
                game.deal_single_card("house")
            
            if house.calculate_hand_val() > 21 or bot2_results[5].calculate_hand_val() > house.calculate_hand_val():
                bot2_results[5].gain_money(bot2_results[4])
                house.lose_money(bot2_results[4])
            
            elif house.calculate_hand_val() > bot2_results[5].calculate_hand_val():
                bot2_results[5].lose_money(bot2_results[4])
                house.gain_money(bot2_results[4])
    
    elif bot2_results[2]:
        while house.calculate_hand_val() < 17 and bot2_results[5].calculate_hand_val() > house.calculate_hand_val():
            game.deal_single_card("house")
                    
        if house.calculate_hand_val() > 21 or bot2_results[5].calculate_hand_val() > house.calculate_hand_val():
            bot2_results[5].gain_money(bot2_results[4])
            house.lose_money(bot2_results[4])
                    
        elif house.calculate_hand_val() > bot2_results[5].calculate_hand_val():
            bot2_results[5].lose_money(bot2_results[4])
            house.gain_money(bot2_results[4])


    # Looking at bot 3
    if bot3_results[3] == "SP":
        if bot3_results[2]:
            if bot3_results[0]:
                while house.calculate_hand_val() < 17 and bot3_results[5].calculate_hand_val() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot3_results[5].calculate_hand_val() > house.calculate_hand_val():
                    bot3_results[5].gain_money(bot3_results[4])
                    house.lose_money(bot3_results[4])
                    
                elif house.calculate_hand_val() > bot3_results[5].calculate_hand_val():
                    bot3_results[5].lose_money(bot3_results[4])
                    house.gain_money(bot3_results[4])

            if bot3_results[1]:
                while house.calculate_hand_val() < 17 and bot3_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot3_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    bot3_results[5].gain_money(bot3_results[4])
                    house.lose_money(bot3_results[4])
                    
                elif house.calculate_hand_val() > bot3_results[5].calculate_hand_val_2():
                    bot3_results[5].lose_money(bot3_results[4])
                    house.gain_money(bot3_results[4])

        elif bot3_results[2]:
            while house.calculate_hand_val() < 17 and bot3_results[5].calculate_hand_val() > house.calculate_hand_val():
                game.deal_single_card("house")
            
            if house.calculate_hand_val() > 21 or bot3_results[5].calculate_hand_val() > house.calculate_hand_val():
                bot3_results[5].gain_money(bot3_results[4])
                house.lose_money(bot3_results[4])
            
            elif house.calculate_hand_val() > bot3_results[5].calculate_hand_val():
                bot3_results[5].lose_money(bot3_results[4])
                house.gain_money(bot3_results[4])

    elif bot3_results[2]:
        while house.calculate_hand_val() < 17 and bot3_results[5].calculate_hand_val() > house.calculate_hand_val():
            game.deal_single_card("house")
                    
        if house.calculate_hand_val() > 21 or bot3_results[5].calculate_hand_val() > house.calculate_hand_val():
            bot3_results[5].gain_money(bot3_results[4])
            house.lose_money(bot3_results[4])
                    
        elif house.calculate_hand_val() > bot3_results[5].calculate_hand_val():
            bot3_results[5].lose_money(bot3_results[4])
            house.gain_money(bot3_results[4])

    # Looking at bot 4
    if bot4_results[3] == "SP":
        if bot4_results[2]:
            if bot4_results[0]:
                while house.calculate_hand_val() < 17 and bot4_results[5].calculate_hand_val() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot4_results[5].calculate_hand_val() > house.calculate_hand_val():
                    bot4_results[5].gain_money(bot4_results[4])
                    house.lose_money(bot4_results[4])
                    
                elif house.calculate_hand_val() > bot4_results[5].calculate_hand_val():
                    bot4_results[5].lose_money(bot4_results[4])
                    house.gain_money(bot4_results[4])

            if bot4_results[1]:
                while house.calculate_hand_val() < 17 and bot4_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot4_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    bot4_results[5].gain_money(bot4_results[4])
                    house.lose_money(bot4_results[4])
                    
                elif house.calculate_hand_val() > bot4_results[5].calculate_hand_val_2():
                    bot4_results[5].lose_money(bot4_results[4])
                    house.gain_money(bot4_results[4])

        elif bot4_results[2]:
            while house.calculate_hand_val() < 17 and bot4_results[5].calculate_hand_val() > house.calculate_hand_val():
                game.deal_single_card("house")
            
            if house.calculate_hand_val() > 21 or bot4_results[5].calculate_hand_val() > house.calculate_hand_val():
                bot4_results[5].gain_money(bot4_results[4])
                house.lose_money(bot4_results[4])
            
            elif house.calculate_hand_val() > bot4_results[5].calculate_hand_val():
                bot4_results[5].lose_money(bot4_results[4])
                house.gain_money(bot4_results[4])
    
    elif bot4_results[2]:
        while house.calculate_hand_val() < 17 and bot4_results[5].calculate_hand_val() > house.calculate_hand_val():
            game.deal_single_card("house")
                    
        if house.calculate_hand_val() > 21 or bot4_results[5].calculate_hand_val() > house.calculate_hand_val():
            bot4_results[5].gain_money(bot4_results[4])
            house.lose_money(bot4_results[4])
                    
        elif house.calculate_hand_val() > bot4_results[5].calculate_hand_val():
            bot4_results[5].lose_money(bot4_results[4])
            house.gain_money(bot4_results[4])

    # Looking at bot 5
    if bot5_results[3] == "SP":
        if bot5_results[2]:
            if bot5_results[0]:
                while house.calculate_hand_val() < 17 and bot5_results[5].calculate_hand_val() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot5_results[5].calculate_hand_val() > house.calculate_hand_val():
                    bot5_results[5].gain_money(bot5_results[4])
                    house.lose_money(bot5_results[4])
                    
                elif house.calculate_hand_val() > bot5_results[5].calculate_hand_val():
                    bot5_results[5].lose_money(bot5_results[4])
                    house.gain_money(bot5_results[4])

            if bot5_results[1]:
                while house.calculate_hand_val() < 17 and bot5_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    game.deal_single_card("house")
                    
                if house.calculate_hand_val() > 21 or bot5_results[5].calculate_hand_val_2() > house.calculate_hand_val():
                    bot5_results[5].gain_money(bot5_results[4])
                    house.lose_money(bot5_results[4])
                    
                elif house.calculate_hand_val() > bot5_results[5].calculate_hand_val_2():
                    bot5_results[5].lose_money(bot5_results[4])
                    house.gain_money(bot5_results[4])

        elif bot5_results[2]:
            while house.calculate_hand_val() < 17 and bot5_results[5].calculate_hand_val() > house.calculate_hand_val():
                game.deal_single_card("house")
            
            if house.calculate_hand_val() > 21 or bot5_results[5].calculate_hand_val() > house.calculate_hand_val():
                bot5_results[5].gain_money(bot5_results[4])
                house.lose_money(bot5_results[4])
            
            elif house.calculate_hand_val() > bot5_results[5].calculate_hand_val():
                bot5_results[5].lose_money(bot5_results[4])
                house.gain_money(bot5_results[4])
    
    
    elif bot5_results[2]:
        while house.calculate_hand_val() < 17 and bot5_results[5].calculate_hand_val() > house.calculate_hand_val():
            game.deal_single_card("house")
                    
        if house.calculate_hand_val() > 21 or bot5_results[5].calculate_hand_val() > house.calculate_hand_val():
            bot5_results[5].gain_money(bot5_results[4])
            house.lose_money(bot5_results[4])
                    
        elif house.calculate_hand_val() > bot5_results[5].calculate_hand_val():
            bot5_results[5].lose_money(bot5_results[4])
            house.gain_money(bot5_results[4])


    # Looking at bot6
    if bot6_results[2]:
        while house.calculate_hand_val() < 17 and bot6_results[5].calculate_hand_val() > house.calculate_hand_val():
            game.deal_single_card("house")
                    
        if house.calculate_hand_val() > 21 or bot6_results[5].calculate_hand_val() > house.calculate_hand_val():
            bot6_results[5].gain_money(bot6_results[4])
            house.lose_money(bot6_results[4])
                    
        elif house.calculate_hand_val() > bot6_results[5].calculate_hand_val():
            bot6_results[5].lose_money(bot6_results[4])
            house.gain_money(bot6_results[4])
    
    print(str(house.hand))
    print()     


# This is the main function that runs the simulation (game)
# Simulation and the Analysis is going to be based on 1000 played hands
def main():

    game_count = 300
    game = Game()
    

    # Percentage of limit, if reached bot takes off
    # 30%
    gain_limit = 13000
    
    print("Welcome to Casino Royale...")
    print("Let's play some blackjack!")
    print()

    bot1_in_game = True
    bot2_in_game = True
    bot3_in_game = True
    bot4_in_game = True
    bot5_in_game = True
    bot6_in_game = True
    
    while game_count > 0:
        
        game.clear_hands()
        game_count -= 1

        house = game.house
        bot1 = game.bot1
        bot2 = game.bot2
        bot3 = game.bot3
        bot4 = game.bot4
        bot5 = game.bot5
        bot6 = game.bot6

        # Looking at the limit gain reached

        if bot1.money >= gain_limit:
            print()
            print("Bot1 made incredible money! Taking off the table...")
            bot1_in_game = False
        
        if bot2.money >= gain_limit:
            print()
            print("Bot2 made incredible money! Taking off the table...")
            bot2_in_game = False
        
        if bot3.money >= gain_limit:
            print()
            print("Bot3 made incredible money! Taking off the table...")
            bot3_in_game = False
        
        if bot4.money >= gain_limit:
            print()
            print("Bot4 made incredible money! Taking off the table...")
            bot4_in_game = False
        
        if bot5.money >= gain_limit:
            print()
            print("Bot5 made incredible money! Taking off the table...")
            bot5_in_game = False
        
        if bot6.money >= gain_limit:
            print()
            print("Bot6 made incredible money! Taking off the table...")
            bot6_in_game = False

        # Looking if bot's are game over

        if bot1.money <= 0:
            print()
            print("Game Over for Bot1...")
            bot1_in_game = False
        
        if bot2.money <= 0:
            print()
            print("Game Over for Bot2...")
            bot2_in_game = False
        
        if bot3.money <= 0:
            print()
            print("Game Over for Bot3...")
            bot3_in_game = False
        
        if bot4.money <= 0:
            print()
            print("Game Over for Bot3...")
            bot4_in_game = False
        
        if bot5.money <= 0:
            print()
            print("Game Over for Bot5...")
            bot5_in_game = False
        
        if bot6.money <= 0:
            print()
            print("Game Over for Bot6...")
            bot6_in_game = False

        if house.money <= 0:
            print("Game Over for House...")
            break
            
        
        print("Let's play a new hand...")
        print()

        print_player_money(house, bot1, bot2, bot3, bot4, bot5, bot6)

        # Betting
        
        if bot1_in_game:
            print()
            print("Bot1 betting....")
            bet = bot1.bet(game)
            print("Bot1: $" + str(bet))
        
        if bot2_in_game:    
            print()
            print("Bot2 betting...")        
            bot2_bet = bot2.bet(game)
            print("Bot2: $" + str(bet))
        
        if bot3_in_game:    
            print()
            print("Bot3 betting...")        
            bot3_bet = bot3.bet(game)
            print("Bot3: $" + str(bot3_bet))
        
        if bot4_in_game:    
            print()
            print("Bot4 betting...")        
            bot4_bet = bot4.bet(game)
            print("Bot4: $" + str(bot4_bet))
        
        if bot5_in_game:    
            print()
            print("Bot5 betting...")        
            bot5_bet = bot5.bet(game)
            print("Bot5: $" + str(bot5_bet))
        
        if bot6_in_game:    
            print()
            print("Bot6 betting...")        
            bot6_bet = bot6.bet(game)
            print("Bot6: $" + str(bot6_bet))

        # Dealing Cards

        print()
        print("Dealing cards...")
        
        game.deal_initial_hands(bot1_in_game, bot2_in_game, bot3_in_game, bot4_in_game, bot5_in_game, bot6_in_game)
        print_initial_cards(house, bot1, bot2, bot3, bot4, bot5, bot6)

        print()
        if bot1_in_game:
            print("Bot1 played...")
            bot1_results = bot1_playing(bot1, house, game, bet)
        else:
            # Just creating a bad result for processing in the house function
            bot1_results = [False,False,False, "", 00, bot1]

        print()
        if bot2_in_game:
            print("Bot2 played...")
            bot2_results = bot2_playing(bot2, house, game, bot2_bet)
        else:
            # Just creating a bad result for processing in the house function
            bot2_results = [False,False,False, "", 00, bot2]

        print()
        if bot3_in_game:
            print("Bot3 played...")
            bot3_results = bot3_playing(bot3, house, game, bot3_bet)
        else:
            # Just creating a bad result for processing in the house function
            bot3_results = [False,False,False, "", 00, bot3]
            
        print()
        if bot4_in_game:
            print("Bot4 played...")
            bot4_results = bot4_playing(bot4, house, game, bot4_bet)
        else:
            # Just creating a bad result for processing in the house function
            bot4_results = [False,False,False, "", 00, bot4]
        
        print()
        if bot5_in_game:
            print("Bot5 played...")
            bot5_results = bot5_playing(bot5, house, game, bot5_bet)
        else:
            # Just creating a bad result for processing in the house function
            bot5_results = [False,False,False, "", 00, bot5]
        
        print()
        if bot6_in_game:
            print("Bot6 played...")
            bot6_results = bot6_playing(bot6, house, game, bot6_bet)
        else:
            # Just creating a bad result for processing in the house function
            bot6_results = [False,False,False, "", 00, bot6]

        print()
        print("House played...")
        house_playing(game, house, bot1_results, bot2_results, bot3_results, bot4_results, bot5_results, bot6_results)

        if game_count == 0:
            print("Simulation finished after playing 300 hands..." )
            print()
            print_player_money(house, bot1, bot2, bot3, bot4, bot5, bot6)    
            print()
            print_calculated_profits(house, bot1, bot2, bot3, bot4, bot5, bot6)
            print()

            
if __name__ == "__main__":
    main()