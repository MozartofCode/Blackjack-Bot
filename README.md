# Blackjack-Bot

Casino Royale is a decentralized casino experience where you play Blackjack against the house alongside with bots that are powered by AI-based decision making algorithms

Initial Blackjack & Bot Project: A previous personal project with Java, where I created a card counting bot
inspired by the movie '21'.

Bots & Analysis: 6 different bots are powered by NN, RL, Decision trees and random forest are playing against the bot and trying to maximize their profits where the performances of each bot is compared based on the performance metric of generating 30% profit

Backend: A MVC structured, decentralized blackjack application where there is a player playing against
the house and the monetary transactions are handled with smart contracts in Solidity. (Developed with the truffle framework and 
deployed an a test blockchain using Ganache)

Frontend: React.js (JS) frontend, Images: https://opengameart.org/


Rules of the Game for this simulation: (https://en.wikipedia.org/wiki/Blackjack)
1- Played with 5 regular decks (52 cards each)
2- One house and 4 players (3 bot and 1 actual player, you)
3- Blackjack by a player pays 3:2 like in a normal casino
4- Doubling and re-splitting after splitting are restricted
5- Insurance bets are not allowed. (Dealer (house) showing an Ace and taking insurance bets)
6- House stays at/above 17
7- Minimum bet is $10 for the game
8- (For the Fullstack application): There is only Hit or Stand possibilities for Player for simplicity
9- (For Bots and CLI application): Actions are hit, stay, double, split and surrender like a normal casino