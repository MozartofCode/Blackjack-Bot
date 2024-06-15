import Card from './Card';
import '../styles/house.css'
import React, { useState, useEffect } from 'react';
import { houseAction, handleHouseBetting, fetchGameState, initializeNewRound } from './blackjackAPI';

const House = ({ house }) => {

  const DownCardImage = require(`../down_card.png`);
  
  const [houseData, setHouseData] = useState(house);
  const [betAmount, setBetAmount] = useState(0);


useEffect(() => {
  const interval = setInterval(async () => {
    const gameState = await fetchGameState();
    setHouseData(gameState.house);
    console.log(gameState.house)

    // If house is not currently in a game, place a bet and take an action
    if (!gameState.house.player_in_game && gameState.house.house_in_game) {
      await handleHouseBet(gameState.house.bet);
      await handleHouseAction();
    }

    // If the round ended keep going with a new one
    else if (!gameState.house.player_in_game && !gameState.house.house_in_game) {
      console.log("Initialized a new round")
      await initializeNewRound()
    }

  }, 1000); // Fetch game state every 1 seconds

  return () => clearInterval(interval);
}, []);



  const handleHouseAction = async () => {
    await houseAction();
    const updatedGameState = await fetchGameState();
    setHouseData(updatedGameState.house);
  };

  const handleHouseBet = async (betAmount) => {
    await handleHouseBetting(betAmount);
    const updatedGameState = await fetchGameState();
    setHouseData(updatedGameState.house);
    setBetAmount(updatedGameState.bet)
  };


  return (
    <div className="player-container">
      <h2>House</h2>
      <div className="cards-container">
      {houseData.cards.map((card, index) => (
          index === 0 && houseData.player_in_game) ? (
            <div key={index} className="card">
              <img src= {DownCardImage} alt="Facedown card" />
            </div>
          ) : (
            <Card key={index} card={card} />
        ))}
      </div>
      <div className="money">Money: ${houseData.money}</div>

    </div>
  );
};

export default House;
