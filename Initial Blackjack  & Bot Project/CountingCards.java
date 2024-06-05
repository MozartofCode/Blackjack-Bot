/// @author: Bertan Berker
///
/// This is a blackjack program in which the Player attempts to double their money with 3 strategies:
/// 1- The MIT Betting Strategy (As portrayed in the movie "21")
/// 2- Basic Strategy (To Decide if a Player should HIT or STAY)
/// 3- Basic Hi-Lo Card Counting Strategy (As portrayed in the movie "21")
///
/// This game is automatically generated so we don't ask for input from the Player
/// The rules are the same as the normal game but player can only HIT or STAY and also,
/// We don't stop until either the PLAYER doubled their money or they are busted!
///
/// Player only starts with $1,000, while the house has $1,000,000
/// The goal for the Player is to double their money!
///
/// At the end of the program, I print the success rate of the player and the number of hands played
/// To show what it took to double player's money


import java.util.ArrayList;
import java.util.Arrays;


public class CountingCards extends BlackJack {

    public static int handPlayed = 0;

    public static int count = 0;

    public static int numberOfWins = 0;

    /// This method implements the betting strategy
    /// Our betting strategy is based on the data we have from counting the cards
    /// Basically the player constantly bets 5% of his account until the
    /// count indicates that we are going to be dealt face cards.
    /// In that case the player bets gradually more of their account 
    /// This is an improvement on the MIT Betting Strategy: For every +2 count:
    /// Amount to Bet = (True Count – 1) * Betting Unit
    /// Minimum Unit = 50 (in our case)
    /// Betting Unit = 200 (in our case)
    /// :return: (int) player's bet

    public static int playerBets() {

        /// True count is count/ remaining number of decks

        double trueCount = count/((double)remainingCards/52);

        int minBet = 10;
        int bettingUnit = 200;

        if (house < minBet) {
            return house;
        }

        else if (player < minBet) {
            return player;
        }

        else if (trueCount >= 2) {      

            int amount = (int)Math.round(trueCount-1) * bettingUnit;
            
            if (player >= amount) {
                return amount;
            } else {
                return player;
            }
        }

        else if (trueCount >= 1) {
            
            int amount = bettingUnit/2;
            
            if (player >= amount) {
                return amount;
            } else {
                return player;
            }
        }

        return minBet;  /// Minimum Bet

    }


    /// This method implements the basic strategy based on the houses hand and players hand
    /// This strategy is very similar to Basic strategy but it has some minor adjustments
    /// :param houseCard: The House's card that is open on the table
    /// :param playerHnad: The player's hand
    /// :precondition: the player's Hand is not over 21
    /// :return: (boolean) true if the player should HIT, false if it should STAY

    public static boolean decideToHit(ArrayList<String> houseCard, ArrayList<String> playerHand) {  

        int houseV = valueCalculation(houseCard);
        int playerV = valueCalculation(playerHand);

        
        if (Arrays.asList(2,3).contains(houseV))  {

            if (playerV >= 4 && playerV <= 7) {return true;}
            else if (playerV == 8) {return true;}
            else if (playerV == 9) {return true;}
            else if (playerV == 10) {return true;}
            else if (playerV == 11) {return true;}
            else if (playerV == 12) {return true;}
            else if (playerV == 13) {return false;}
            else if (playerV == 14) {return false;}
            else if (playerV == 15) {return false;}
            else if (playerV == 16) {return false;}
            else if (playerV >= 17) {return false;}

       } else if (Arrays.asList(4,5,6).contains(houseV)) {

            if (playerV >= 4 && playerV <= 7) {return true;}
            else if (playerV == 8) {return true;}
            else if (playerV == 9) {return true;}
            else if (playerV == 10) {return true;}
            else if (playerV == 11) {return true;}
            else if (playerV == 12) {return false;}
            else if (playerV == 13) {return false;}
            else if (playerV == 14) {return false;}
            else if (playerV == 15) {return false;}
            else if (playerV == 16) {return false;}
            else if (playerV >= 17) {return false;}

        
       } else if (Arrays.asList(7,8,9,10,11).contains(houseV)) {

            if (playerV >= 4 && playerV <= 7) {return true;}
            else if (playerV == 8) {return true;}
            else if (playerV == 9) {return true;}
            else if (playerV == 10) {return true;}
            else if (playerV == 11) {return true;}
            else if (playerV == 12) {return true;}
            else if (playerV == 13) {return true;}
            else if (playerV == 14) {return true;}
            else if (playerV == 15) {return true;}
            else if (playerV == 16) {return true;}
            else if (playerV >= 17) {return false;}

       }

       return true;
    }
    

    /// This method helps the player with counting cards
    /// :param Card: Represents a card, in the format "A" or "10"

    public static void countCards(String card) {    
        
        /// Cards [2, 6] have the value of + 1
        /// Cards [7. 9] have the value of 0
        /// Cards [10, A] have the value of -1

        ArrayList<String> plusOne = new ArrayList<String>() {
            {
                add("2");
                add("3");
                add("4");
                add("5");
                add("6");
            }
        };

        ArrayList<String> minusOne = new ArrayList<String>() {
            {
                add("A");
                add("K");
                add("Q");
                add("J");
                add("10");
            }
        };

        if (plusOne.contains(card)) {
            count++;
        }

        else if (minusOne.contains(card)) {
            count--;
        }
    }    

    /// This is the method that coordinates everything and automates the game
    /// :param bet: Player's bet

    public static void automatedGamePlay(int bet) {

         /// Initializing the values and the piles of the house and the player

         int valuePlayer = 0;
         int valueHouse = 0;
         ArrayList<String> playerPile = new ArrayList<>();
         ArrayList<String> housePile = new ArrayList<>();
         ArrayList<String> houseCard = new ArrayList<>();
 
 
         /// Giving each side 2 cards (Initially dealing) - House only shows one card (CARD)
         /// It's in the format "K-10" for two cards
         /// Cardcounting function is added to count cards
 
         String[] twoCardsHouse = drawCard(deckID, true).split("-");   
         String[] twoCardsPlayer = drawCard(deckID, true).split("-");

         houseCard.add(twoCardsHouse[0]);
         countCards(twoCardsHouse[0]);
         countCards(twoCardsHouse[1]);
         countCards(twoCardsPlayer[0]);
         countCards(twoCardsPlayer[1]);
 
         System.out.println("");
         System.out.println("House: " + twoCardsHouse[0] + " CARD");
         System.out.println("Player: " + twoCardsPlayer[0] + " " + twoCardsPlayer[1]);
         System.out.println("");
 
 
         /// Value calculation
 
         playerPile.add(twoCardsPlayer[0]);
         playerPile.add(twoCardsPlayer[1]);
         housePile.add(twoCardsHouse[0]);
         housePile.add(twoCardsHouse[1]);
 
         valuePlayer = valueCalculation(playerPile);
         valueHouse = valueCalculation(housePile);
 
 
         /// If player is dealt 21 player gets 1.5 worth of their bet
 
         if (valuePlayer == 21) {
             System.out.println("BlackJack!!!");
             System.out.println("");
             player += bet * (1.5);
             house -= bet * (1.5);
         }
 
         else {
             
             /// Ask player to hit or stay
             /// if player is bigger than 21 he automatically loses
 
             boolean stay = false;
 
             while (!stay && valuePlayer <= 21) {
 
                 boolean hit = decideToHit(houseCard, playerPile);
 
                 if (hit) {
 
                     /// The format of a single card is like 10
                     /// Adding the card Counting function
                    
                     String newCard = drawCard(deckID, false);  

                     countCards(newCard);
 
                     System.out.println("");
                     System.out.println("House: " + twoCardsHouse[0] + " CARD");
                     System.out.print("Player: " );
                     for (int i = 0; i < playerPile.size(); i++) {
                         System.out.print(playerPile.get(i) + " ");
                     }
                     System.out.println(newCard);
                     System.out.println("");
 
                     playerPile.add(newCard);
                     valuePlayer = valueCalculation(playerPile);
                 }
 
                 else {
                     stay = true;
                 }
             }
 
             if (valuePlayer > 21) {
                 System.out.print("House: ");
                 for (int i = 0; i < housePile.size(); i++) {
                     System.out.print(housePile.get(i) + " ");
                 }
                 
                 System.out.println("");
 
                 System.out.print("Player: " );
                 for (int i = 0; i < playerPile.size(); i++) {
                     System.out.print(playerPile.get(i) + " ");
                 }
 
                 System.out.println("");
                 System.out.println("");
 
                 System.out.println("The Player is over 21! The Player lost...");
                 System.out.println("");
                 player -= bet;
                 house += bet;
             }
             
             else {
             
                 /// House's Turn
                 /// If House is 17 or bigger it has to stay
                 /// If not, the House checks the hands value and if that is less then player
                 /// House hits until it either gets busted or surpasses the player or surpasses number 17
                 /// If at the end, House is not bust then we compare its value with the
                 /// player and basically whoever is bigger wins
 
                 if (valueHouse < 17) {
                     if (valuePlayer < valueHouse) {
                         System.out.println("");
                         System.out.print("House: ");
                         for (int i = 0; i < housePile.size(); i++) {
                             System.out.print(housePile.get(i) + " ");
                         }
     
                         System.out.println("");
         
                         System.out.print("Player: " );
                         for (int i = 0; i < playerPile.size(); i++) {
                             System.out.print(playerPile.get(i) + " ");
                         }
 
                         System.out.println("");
                         System.out.println("");
 
                         System.out.println("The House wins!");
                         System.out.println("");
                         player -= bet;
                         house += bet;
                     }
 
                     else if (valueHouse == valuePlayer) {      
                         System.out.println("");                  
                         System.out.print("House: ");
                         for (int i = 0; i < housePile.size(); i++) {
                             System.out.print(housePile.get(i) + " ");
                         }
 
                         System.out.println("");
     
                         System.out.print("Player: " );
                         for (int i = 0; i < playerPile.size(); i++) {
                             System.out.print(playerPile.get(i) + " ");
                         }
 
                         System.out.println("");
                         System.out.println("");
 
                         System.out.println("It's a tie!");
                         System.out.println("");
                     }
 
                     else {
                         
                         /// House has to hit here to surpass the player and win
 
                         while (valueHouse < 17 && valueHouse < valuePlayer) {
                             
                             String newCard = drawCard(deckID, false); 

                             countCards(newCard);
 
                             System.out.println("");
                             
                             System.out.print("House: ");
                             for (int i = 0; i < housePile.size(); i++) {
                                 System.out.print(housePile.get(i) + " ");
                             }
 
                             System.out.println(newCard);
         
                             System.out.print("Player: " );
                             for (int i = 0; i < playerPile.size(); i++) {
                                 System.out.print(playerPile.get(i) + " ");
                             }
         
                             System.out.println("");
                             System.out.println("");
 
                             housePile.add(newCard);
                             valueHouse = valueCalculation(housePile);

                         }
 
                         if (valueHouse > 21) {
                             System.out.print("House: ");
                             for (int i = 0; i < housePile.size(); i++) {
                                 System.out.print(housePile.get(i) + " ");
                             }
                             
                             System.out.println("");
             
                             System.out.print("Player: " );
                             for (int i = 0; i < playerPile.size(); i++) {
                                 System.out.print(playerPile.get(i) + " ");
                             }
 
                             System.out.println("");
                             System.out.println("");
 
                             System.out.println("House is over 21! Player wins...");
                             System.out.println("");
                             player += bet;
                             house -= bet;    
                         }
 
                         else if (valuePlayer < valueHouse) {
                             
                             System.out.print("House: ");
                             for (int i = 0; i < housePile.size(); i++) {
                                 System.out.print(housePile.get(i) + " ");
                             }
         
                             System.out.println("");
             
                             System.out.print("Player: " );
                             for (int i = 0; i < playerPile.size(); i++) {
                                 System.out.print(playerPile.get(i) + " ");
                             }
 
                             System.out.println("");
                             System.out.println("");
 
                             System.out.println("The House wins!");
                             System.out.println("");
                             player -= bet;
                             house += bet;
                         }
     
                         else if (valueHouse == valuePlayer) {
                             
                             System.out.print("House: ");
                             for (int i = 0; i < housePile.size(); i++) {
                                 System.out.print(housePile.get(i) + " ");
                             }
         
                             System.out.println("");
             
                             System.out.print("Player: " );
                             for (int i = 0; i < playerPile.size(); i++) {
                                 System.out.print(playerPile.get(i) + " ");
                             }
 
                             System.out.println("");
                             System.out.println("");
 
                             System.out.println("It's a tie!");
                             System.out.println("");
                         }
 
                        }
                    }
 
                 else { 
 
                     if (valuePlayer < valueHouse) {
                         System.out.print("House: ");
                         for (int i = 0; i < housePile.size(); i++) {
                             System.out.print(housePile.get(i) + " ");
                         }
     
                         System.out.println("");
         
                         System.out.print("Player: " );
                         for (int i = 0; i < playerPile.size(); i++) {
                             System.out.print(playerPile.get(i) + " ");
                         }
 
                         System.out.println("");
                         System.out.println("");
 
                         System.out.println("The House wins!");
                         System.out.println("");
                         player -= bet;
                         house += bet;
                     }
 
                     else if (valueHouse == valuePlayer) {
                         System.out.print("House: ");
                         for (int i = 0; i < housePile.size(); i++) {
                             System.out.print(housePile.get(i) + " ");
                         }
     
                         System.out.println("");
         
                         System.out.print("Player: " );
                         for (int i = 0; i < playerPile.size(); i++) {
                             System.out.print(playerPile.get(i) + " ");
                         }
 
                         System.out.println("");
                         System.out.println("");
 
                         System.out.println("It's a tie!");
                         System.out.println("");
                     }
 
                     else {
                         System.out.print("House: ");
                         for (int i = 0; i < housePile.size(); i++) {
                             System.out.print(housePile.get(i) + " ");
                         }
                         
                         System.out.println("");
     
                         System.out.print("Player: " );
                         for (int i = 0; i < playerPile.size(); i++) {
                             System.out.print(playerPile.get(i) + " ");
                         }
 
                         System.out.println("");
                         System.out.println("");
 
                         System.out.println("Player wins!");
                         System.out.println("");
                         player += bet;
                         house -= bet;
                     } 
                 }
             }
         }

    }
    

    /// This is the main function that starts the application plays the game with the 
    /// Help of other functions that it calls
    /// :param args: Array of Strings that are passed to the "main" function

    public static void main(String[] args) {
        welcome();
        printAccounts();
        gameSetup();
        
        while (player < 2000 && player > 0) {

            handPlayed++;

            int tempAccount = player;

            /// Betting process...
            int bet = playerBets();
            placeBet(bet);

            /// Playing process...
            automatedGamePlay(bet);

            /// Paying process...
            printAccounts();

            if (tempAccount < player) {
                numberOfWins++;
            }

            if (remainingCards <= 165) {
                /// Reshuffling the cards when the deck is nearly halfway done
                count = 0;
                remainingCards = 312;
                gameSetup();
            }
        }

        System.out.println("");
        System.out.println("Total Hands played: " + handPlayed);
        System.err.printf("Success Rate of Player: %.2f", (double) numberOfWins/handPlayed);
        System.out.println("");
        System.out.println("");
     
        if (player <= 0) {    
            System.out.println("Player lost! Better luck next time...");
            System.out.println("");;
        }

        else {
            System.out.println("Congratulations! Player more than doubled their money...");
            System.out.println("");
        }

    }   
}