# @Author: Bertan Berker
# @Filename: player_vs_house.py
# This is the version of the simulation where it's player vs house only (no bots)

from gameplay import Game
import csv

# This function is used for generating data for the csv that will be used by bot2 (NN)
# :param data_row: one row of data to be added to the csv file 
# [player_hand, dealer_hand, count, move, bet]
def generate_csv_dataset(data_row, dataset_name):
    filename = dataset_name

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_row)


# This function/main is used for simulating a game where it's player (me) against the house
# Mainly useful for also generating data that will be used for training bot3 (the second NN based bot)
# I'll be playing kind of randomly (within reason still) to generate some data, no card counting or cheating
def main():
    game = Game()
    game_count = 100

    print("Welcome to Casino Royale...")
    print("Let's play some blackjack!")
    print()
    
    while game_count > 0:
        
        game.clear_hands()
        game_count -= 1

        house = game.house
        player = game.player

        
        if player.money <= 0:
            
            print()
            print("Game Over for Player...")
            break

        elif house.money <= 0:
            print("Game Over for House...")
            break
        
        print("Let's play a new hand...")
        print()

        print("Your Money: " + str(player.money))

        print()
        bet = int(input("Player is betting: "))
        print("Player bets $" + str(bet))

        print()
        print("Dealing cards...")
        game.deal_initial_hands()
        print("House: " + str(house.hand[0]))
        print("Player: " + str(player.hand))
        print()

        playing = True
        
        # For split functionality
        playing_1 = True
        playing_2 = True

        if player.is_21():
            print("Blackjack!")
            playing = False
            player.gain_money(3 * bet // 2)
            house.lose_money(3 * bet // 2)

        else:
            move = input("What do you want to do? (H/S/SU/SP/D): ")

            # Adding the play to the csv file
            data_row = [list(player.hand), house.hand[0], game.card_count, move, bet]
            generate_csv_dataset(data_row, "blackjack_dataset_player.csv")


            if move == "H":
                
                game.deal_single_card("player")
                
                print("Player: " + str(player.hand))

                while not player.is_over_21():
                    new_move = input("Now what's new move?(H/S): ")
                    if new_move == "H":
                        game.deal_single_card("player")                
                        print("Player: " + str(player.hand))
                    else:
                        break

                if player.is_over_21():
                    player.lose_money(bet)
                    house.gain_money(bet)
                    playing = False

            elif move == "S":
                player.stand()    

            elif move == "SU":
                player.surrender(bet)
                house.gain_money(bet//2)
                playing = False

            elif move == "SP":
                if player.money >= bet:
                    
                    # Two separate hands
                    player.hand2.append(player.hand[-1])
                    player.hand.pop()

                    # For Hand1:
                    game.deal_single_card("player")
                    game.deal_single_card_2("player")
                                
                    print("Player hand: " + str(player.hand))
                    print("Player hand2: " + str(player.hand2))

                    if player.is_21():
                        print("Blackjack!")
                        playing_1 = False
                        player.gain_money(3 * bet // 2)
                        house.lose_money(3 * bet // 2)

                    else:
                        while not player.is_over_21():
                            new_move = input("Now what's new move for hand1?(H/S): ")
                            if new_move == "H":
                                game.deal_single_card("player")                        
                                print("Player: " + str(player.hand))
                            else:
                                break

                        if player.is_over_21():
                            player.lose_money(bet)
                            house.gain_money(bet)
                            playing_1 = False


                    # For Hand2:                
                    if player.calculate_hand_val_2() == 21:
                        print("Blackjack!")
                        playing_2 = False
                        player.gain_money(3 * bet // 2)
                        house.lose_money(3 * bet // 2)
                    
                    else:
                        while player.calculate_hand_val_2() < 21:
                            new_move = input("Now what's new move for hand2?(H/S): ")
                            if new_move == "H":
                                game.deal_single_card_2("player")                        
                                print("Player: " + str(player.hand2))
                            else:
                                break

                        if player.calculate_hand_val_2() > 21:
                            player.lose_money(bet)
                            house.gain_money(bet)
                            playing_2 = False

            elif move == "D":
                if player.money >= bet:
                    game.deal_single_card("player")
                    bet += bet

                    if player.is_over_21():
                        player.lose_money(bet)
                        house.gain_money(bet)
                        playing = False

            
            if move != "SP":
                print(str(player.hand))

            else:
                if not playing_1 and not playing_2:
                    playing = False

                print(str(player.hand))
                print(str(player.hand2))


        print()
        print("House played...")
        
        if move == "SP":
            if playing:
                if playing_1: 
                    while house.calculate_hand_val() < 17 and player.calculate_hand_val() > house.calculate_hand_val():
                        game.deal_single_card("house")                
                        print("House: " + str(house.hand))
                    
                    if house.calculate_hand_val() > 21 or player.calculate_hand_val() > house.calculate_hand_val():
                        player.gain_money(bet)
                        house.lose_money(bet)
                    
                    elif house.calculate_hand_val() > player.calculate_hand_val():
                        player.lose_money(bet)
                        house.gain_money(bet)
                        

                if playing_2:
                    
                    while house.calculate_hand_val() < 17 and player.calculate_hand_val_2() > house.calculate_hand_val():
                        game.deal_single_card("house")
                        print("House: " + str(house.hand))
                    
                    if house.calculate_hand_val() > 21 or player.calculate_hand_val_2() > house.calculate_hand_val():
                        player.gain_money(bet)
                        house.lose_money(bet)
                    
                    elif house.calculate_hand_val() > player.calculate_hand_val_2():
                        player.lose_money(bet)
                        house.gain_money(bet)

        elif playing:

            while house.calculate_hand_val() < 17 and player.calculate_hand_val() > house.calculate_hand_val():
                game.deal_single_card("house")            
                print("House: " + str(house.hand))
            
            if house.calculate_hand_val() > 21 or player.calculate_hand_val() > house.calculate_hand_val():
                player.gain_money(bet)
                house.lose_money(bet)
            
            elif house.calculate_hand_val() > player.calculate_hand_val():
                player.lose_money(bet)
                house.gain_money(bet)
            
        print(str(house.hand))

        print()     

        if game_count == 0:
            print("Simulation finished after playing 1000 hands..." )
            print()
            print("Each players money:")
            print("House: $" + str(house.money))
            print("Player: $" + str(player.money))
            print()
