/// @author: Bertan Berker
/// This is a blackjack game
/// The computer is the House and you are playing against it by yourself
/// The API I use for shuffling the card decks and drawing a card is https://deckofcardsapi.com/ 
/// This whole project has been inspired by one of my favorite movies "21"


import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Scanner;  

public class BlackJack {


    public static String deckID = "";

    public static int remainingCards = 312;

    public static int house = 1000000;     /// Money House has

    public static int player = 1000;        /// Money Player has


    /// This method prints the money house and player has

    public static void printAccounts () {
        System.err.println("");
        System.out.println("The Accounts are:");
        System.err.println("House's Account: $" + house);
        System.err.println("Player's Account: $" + player);
    }


    /// This method prints the welcome message

    public static void welcome() {
        System.err.println("");
        System.out.println("Welcome to Las Vegas...");
        System.out.println("");
        System.err.println("Let's play some BlackJack!");
        System.out.println("");
        System.out.println("There are 6 decks in play and the game goes on until " +
         "either the house or the player goes bankrupt...");
        System.out.println("You can only hit or stay and house can't hit if it is 17 or higher. " +
        "If you are dealt a blackjack, you get 1.5 times your bet...");
        System.out.println("");
        System.err.println("So let's start!");
        System.out.println(""); 
    }


    /// This method asks the user how much they want to bet
    /// :return: (int) user's bet

    public static int askPlayerBet() {
        
        String bet = "";

        while (bet.length() == 0) {
            System.out.println("");
            Scanner myObj = new Scanner(System.in);  /// Create a Scanner object
            System.out.print("How much would you like to bet?: ");
            String inputUser = myObj.nextLine();  /// Reads user input

            try {
                Integer.parseInt(inputUser);

                if (Integer.parseInt(inputUser) <= player) {
                    bet = inputUser;
                }
    
                else if (Integer.parseInt(inputUser) > house) {
                    System.out.println("House doesn't have that much money. " +
                    "The max amount you can bet is the amount House has.");
                }
    
                else {
                    System.out.println("You don't have that much money! Try again...");
                }

            } catch (NumberFormatException nfe) {
                System.out.println("You can only give numeric characters as input. Ex: 100 ");
            }
        }

        return Integer.parseInt(bet);
    }


    /// This method prints the bets
    /// House must automatically match the player
    /// :param playerBet: the Player's bet

    public static void placeBet(int playerBet) {
        System.out.println("");
        System.err.println("The bets:");
        System.err.println("Player: $" + playerBet);
        System.err.println("House: $" + playerBet);
    }


    /// This method gets the shuffled 6 deck of cards from the API with a GET request

    public static void gameSetup() {

        String cards = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6";

        try {
			URL url = new URL(cards);
			HttpURLConnection conn = (HttpURLConnection)url.openConnection();
			conn.setRequestMethod("GET");
			conn.connect();
			if(conn.getResponseCode() == 200) {
				Scanner scan = new Scanner(url.openStream());
				while(scan.hasNext()) {
					String temp = scan.nextLine();
                  	
                    /// Parsing the JSON here

                    String[] parts = temp.split(",");

                    String[] id = parts[1].split(":");

                    deckID = id[1].substring(2, id[1].length()-1);
                }
            }
        } catch (MalformedURLException err) {
            System.out.println(err);
        } catch (IOException err) {
            System.out.println(err);
        }
    }


    /// This method sends an API request to draw a card from the deck
    /// :param deckID: the Deck's unique ID for the API Request
    /// :param initialDealing: Boolean value that represents if we should draw two cards
    /// :return: (String) the card(s)

    public static String drawCard(String deckID, boolean initialDealing) {

        String cards = "";
        String card = "";

        if (initialDealing) {   /// Drawing two cards for the initial dealing of cards

                remainingCards -= 2;

                for (int j = 0; j < 2; j++) {

                    String draw = "https://deckofcardsapi.com/api/deck/" + deckID + "/draw/?count=1";
                    
                    try {
                        URL url = new URL(draw);
                        HttpURLConnection conn = (HttpURLConnection)url.openConnection();
                        conn.setRequestMethod("GET");
                        conn.connect();
                        if(conn.getResponseCode() == 200) {
                            Scanner scan = new Scanner(url.openStream());
                            while(scan.hasNext()) {
                                String temp = scan.nextLine();
                                
                                /// Parsing the JSON here

                                int indexOfValue = temp.indexOf("\"value\"" + ": ") + 10;

                                card = temp.substring(indexOfValue, indexOfValue+2);

                                if (card.length() == 2 && card.substring(1).equals("\"")) {
                                    card = card.replace("\"", "");
                                }

                                else if (card.equals("AC")) {
                                    card = "A";
                                }
                                else if (card.equals("JA")) {
                                    card = "J";
                                }
                                else if (card.equals("QU")) {
                                    card = "Q";
                                }
                                else if (card.equals("KI")) {
                                    card = "K";
                                }

                                cards += card;

                                if (j == 0) {
                                    cards += "-";
                                }

                            }
                        }

                    } catch (MalformedURLException err) {
                        System.out.println(err);
                    } catch (IOException err) {
                        System.out.println(err);
                    }
            }
        }

        else {

            remainingCards -= 1;

            String draw = "https://deckofcardsapi.com/api/deck/" + deckID + "/draw/?count=1";

            try {
                URL url = new URL(draw);
                HttpURLConnection conn = (HttpURLConnection)url.openConnection();
                conn.setRequestMethod("GET");
                conn.connect();
                if(conn.getResponseCode() == 200) {
                    Scanner scan = new Scanner(url.openStream());
                    while(scan.hasNext()) {
                        String temp = scan.nextLine();
                        
                        /// Parsing the JSON here

                        int indexOfValue = temp.indexOf("\"value\"" + ": ") + 10;

                        cards = temp.substring(indexOfValue, indexOfValue+2);

                        if (cards.length() == 2 && cards.substring(1).equals("\"")) {
                            cards = cards.replace("\"", "");
                        }

                        else if (cards.equals("AC")) {
                            cards = "A";
                        }
                        else if (cards.equals("JA")) {
                            cards = "J";
                        }
                        else if (cards.equals("QU")) {
                            cards = "Q";
                        }
                        else if (cards.equals("KI")) {
                            cards = "K";
                        }
                    }
                }

            } catch (MalformedURLException err) {
                System.out.println(err);
            } catch (IOException err) {
                System.out.println(err);
            }
            
        }

        return cards;
    }


    /// This method calculates the value of our hand
    /// :param pile: represents the cards in your hand
    /// :return: (int) the value that your hand represents

    public static int valueCalculation(ArrayList<String> pile) {

        int value = 0;

        ArrayList<String> faceValues = new ArrayList<String>() {    /// FaceValues have a value of 10
            {
                add("K");
                add("Q");
                add("J");
            }
        };
        
        int isThereA = 0; // changes based on the number of As in the pile
        int lowA = 1;
        int highA = 11;

        for (int i = 0; i < pile.size(); i++) {
            
            String card = pile.get(i);

            if (faceValues.contains(card)) {
                value += 10;
            }

            else if (!card.equals("A")) {
                value += Integer.parseInt(card);
            }

            else {
                isThereA += 1;
            }
        }

        /// Checking for As in the pile, A can be 1 or 11

        if (isThereA > 0) {

            if (value + highA > 21) {
                while (isThereA > 0) {
                    value += lowA;
                    isThereA--;
                }
            }
            else if (isThereA == 1 && (value + highA == 21)) {
                value += highA;
            }
            else if (value + highA < 21) {

                if (isThereA == 1) {
                    value += highA;
                }
                else {
                    while (isThereA > 0) {

                        if (value + highA >= 21) {
                            value += lowA;
                        }    
                        else if (value + highA < 21) {
                            value += highA;
                        }
                        isThereA--;
                    }

                }
            }
    
        }

        return value;
    }


    /// This method asks for user's input about whether to HIT or STAY
    /// :return: (boolean) true if user wants to hit

    public static boolean askHitStay() {

        String answer = "";

        while (answer.length() == 0) {

            System.out.println("");
            Scanner myObj = new Scanner(System.in);  /// Create a Scanner object
            System.out.print("Do you want to hit or stay? (HIT or STAY): ");
            String inputUser = myObj.nextLine();  /// Reads user input

            if (inputUser.equals("HIT")) {
                answer = "HIT";
            } else if (inputUser.equals("STAY")) {
                answer = "STAY";
            } else {
                System.out.println("Inappropriate command! Command can either be HIT or STAY!!");
            }
        }

        if (answer.equals("HIT")) {
            return true;  /// HIT
        }    
           
        return false; /// STAY
    }


    /// This method is the main gaming method that coordinates everything
    /// :param bet: User's bet

    public static void gamePlay(int bet) {

        /// Initializing the values and the piles of the house and the player

        int valuePlayer = 0;
        int valueHouse = 0;
        ArrayList<String> playerPile = new ArrayList<>();
        ArrayList<String> housePile = new ArrayList<>();


        /// Giving each side 2 cards (Initially dealing) - House only shows one card (CARD)
        /// It's in the format "K-10" for two cards

        String[] twoCardsHouse = drawCard(deckID, true).split("-");   
        String[] twoCardsPlayer = drawCard(deckID, true).split("-");

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

                boolean hit = askHitStay();

                if (hit) {

                    /// The format of a single card is like 10

                    String newCard = drawCard(deckID, false);  

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


    /// This method asks for user input about whether they want to keep playing or not
    /// :return: true if They want to keep playing

    public static boolean stayOnTable() {

        String answer = "";

        while (answer.length() == 0) {

            System.out.println("");
            Scanner myObj = new Scanner(System.in);  /// Create a Scanner object
            System.out.print("Do you want to keep playing? (YES or NO): ");
            String inputUser = myObj.nextLine();  /// Reads user input

            if (inputUser.equals("YES")) {
                answer = "YES";
            } else if (inputUser.equals("NO")) {
                answer = "NO";
            } else {
                System.out.println("Inappropriate command! Command can either be YES or NO!!");
            }
        }

        if (answer.equals("YES")) {
            return true;  /// YES
        }    
           
        return false; /// NO
    }


    /// This is the main function that starts the application plays the game with the 
    /// Help of other functions that it calls
    /// :param args: Array of Strings that are passed to the "main" function

    public static void main(String[] args) {
        
        welcome();
        printAccounts();
        gameSetup();

        boolean playing = true;
        
        while (house > 0 && player > 0 && playing) {

            /// Betting process...
            int bet = askPlayerBet();
            placeBet(bet);

            /// Playing process...
            gamePlay(bet);

            /// Paying process...
            printAccounts();

            if (remainingCards <= 165) {
                /// Reshuffling the cards when the deck is nearly halfway done
                remainingCards = 312;
                gameSetup();
            }

            if (house > 0 && player > 0) {
                playing = stayOnTable();
            }

        }

        System.out.println("");

        if (player <= 0) {
            System.out.println("Player lost! Better luck next time...");
        }

        else if (playing == false) {
            System.out.println("Thank you for visiting our Casino...");
            printAccounts();
        }

        else {
            System.out.println("The house went bankrupt! Don't come back here again...");
        }
        System.out.println("");
    }   
}