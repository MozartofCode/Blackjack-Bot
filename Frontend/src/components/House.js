import Card from './Card';
import '../styles/house.css'
import React, { useState, useEffect } from 'react';
import { houseAction, handleHouseBetting, fetchGameState } from './blackjackAPI';

const House = ({ house }) => {

  const DownCardImage = require(`../down_card.png`);
  
  const [playerData, setHouseData] = useState(house);
  const [betAmount, setBetAmount] = useState(0);
  
  useEffect(() => {


    const initializeHouse = async () => {
      const gameState = await fetchGameState();
      
      console.log(gameState.house)
      setHouseData(gameState.house);

       // If house is not currently in a game, place a bet and take an action
       if (!gameState.house.player_in_game) {
        await handleHouseBet(gameState.house.bet);
        await handleHouseAction();
      }

    };
    initializeHouse();
}, [playerData]);

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
      {house.cards.map((card, index) => (
          index === 0 ? (
            <div key={index} className="card">
              <img src= {DownCardImage} alt="Facedown card" />
            </div>
          ) : (
            <Card key={index} card={card} />
          )
        ))}
      </div>
      <div className="money">Money: ${house.money}</div>




    </div>
  );
};

export default House;
