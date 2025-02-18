# Blackjack-Bot

Play Blackjack against the house alongside AI-powered bots using advanced decision-making algorithms. This decentralized application (DApp) integrates blockchain-based monetary transactions and AI-driven strategy optimization.


📌 Overview

Casino Royale is a decentralized Blackjack experience where players compete against the house alongside AI-driven bots. The project combines smart contracts, machine learning-based decision-making, and blockchain technology to create a next-generation casino experience. <br>


🔥 Key Features

✅ AI-Powered Bots – Compete against six different bots powered by Neural Networks (NN), Reinforcement Learning (RL), Decision Trees, and Random Forests.

✅ Decentralized Blackjack DApp – Built using Solidity smart contracts, deployed via Truffle on a test blockchain using Ganache.

✅ MVC-Structured Backend – Clean, scalable, and modularized architecture.

✅ React.js Frontend – Interactive UI for seamless gameplay.

✅ Fair & Transparent Transactions – Smart contracts ensure fair payouts and decentralized casino operations.


🏗️ Tech Stack

Backend: Solidity (Smart Contracts), Truffle, Ganache, Node.js

Frontend: React.js

AI Models: Neural Networks (NN), Reinforcement Learning (RL), Decision Trees, Random Forests

Blockchain: Ethereum (Testnet), Web3.js

Development Tools: Python, Java (for early bot development), OpenGameArt (for assets)



🎮 Game Rules

Casino Royale follows a structured set of rules inspired by traditional Blackjack:

1️⃣ Played with 5 standard decks (52 cards each).

2️⃣ One house (dealer) vs. four players (3 AI bots + 1 human player).

3️⃣ Blackjack pays 3:2, as in real casinos.

4️⃣ Doubling and re-splitting after a split are restricted.

5️⃣ No insurance bets (dealer showing an Ace does not allow insurance).

6️⃣ Dealer must stand on 17 or above.

7️⃣ Minimum bet: $10.

8️⃣ Player can only Hit or Stand in the full-stack DApp for simplicity.

9️⃣ Bots in the CLI version can Hit, Stand, Double, Split, or Surrender like in a real casino.




🛠️ Installation & Setup


**Backend (Solidity + Smart Contracts) Setup**

1. Clone the repository:
   
git clone https://github.com/MozartofCode/Blackjack-Bot.git

cd Casino-Royale

2. Install dependencies:
   
npm install -g truffle

npm install

3. Start a local blockchain:
   
ganache-cli


4. Deploy the smart contracts:
   
truffle migrate --reset



**Frontend (React.js) Setup**


1. Navigate to the frontend directory:
   
cd client


2. Install dependencies:
   
npm install


3. Run the frontend:
   
npm start



**Bots & AI Analysis**

python bot_analysis.py

This script runs AI-powered bots against the house and evaluates profitability based on a 30% profit threshold.


📊 AI Bot Analysis

The AI models are trained to maximize profits using various strategies:

Neural Networks (NN) – Self-learning bot that adapts based on game outcomes.

Reinforcement Learning (RL) – Uses Q-learning to optimize decision-making.

Decision Trees & Random Forests – Predicts the best moves based on historical game data.

Random Bot – A baseline comparison using purely random moves.

Each bot's win rate and profit percentage are analyzed over thousands of games to determine the most effective strategy.



🚧 Future Enhancements

🔹 Integrate a Metamask Web3 wallet for real blockchain transactions.

🔹 Expand AI strategies with Deep Q Networks (DQN).

🔹 Implement additional Blackjack features like splitting, doubling down, and insurance in the DApp version.

🔹 Multiplayer support for real-time decentralized gameplay.



🏆 Project Inspiration

This project was inspired by the movie "21", where a team of MIT students successfully applied card counting strategies to Blackjack. The initial bot was built in Java and later evolved into an AI-powered system with advanced ML models.


🤝 Contributing

Contributions are welcome! Feel free to fork the repo, open issues, or submit pull requests.
