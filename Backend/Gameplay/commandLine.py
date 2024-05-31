# This is a basic command line version of the frontend for further analysis of the performance of the bots

import basics


def calculate_game_stats():
    return

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


def main():

    game = basics.Game()
    house = game.house
    bot1 = game.bot1
    bot2 = game.bot2
    bot3 = game.bot3

    print("Welcome to Casino Royale...")
    print("Let's play some blackjack!")
    print()

    print_player_money(house, bot1, bot2, bot3)

    print()
    print("Dealing cards...")
    game.deal_initial_hands()
    print()

    print_player_cards(house, bot1, bot2, bot3)

    print()

    print("Bot1 playing....")
    #TODO: BOT1 play
    print()

    print("Bot2 playing....")
    #TODO: BOT2 play
    print()

    print("Bot3 playing....")
    #TODO: BOT3 play
    print()


    






if __name__ == "__main__":
    main()