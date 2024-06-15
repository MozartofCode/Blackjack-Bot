import React from 'react';
import Card from './Card';
import '../styles/player.css'; 
import { playerAction, handlePlayerBet, fetchGameState } from './blackjackAPI';
import { useState, useEffect } from 'react';

const Player = ({ player }) => {
  
  const [playerData, setPlayerData] = useState(player);
  const [betAmount, setBetAmount] = useState(0);
  const [inPlay, setInPlay] = useState(false);

useEffect(() => {
  const interval = setInterval(async () => {
    const gameState = await fetchGameState();
    setPlayerData(gameState.player);
    console.log(gameState.player)

  }, 1000); // Fetch game state every 1 seconds

  return () => clearInterval(interval);
}, []);


  const handlePlayerAction = async (action) => {
    await playerAction(action);
    const updatedGameState = await fetchGameState();
    setPlayerData(updatedGameState.player);
  };

  const handleBet = async (betAmount) => {
    setInPlay(true);
    await handlePlayerBet(betAmount);
    const updatedGameState = await fetchGameState();
    setPlayerData(updatedGameState.player);
    setBetAmount(updatedGameState.bet)
  };
  
  return (
    
    <div className="player-container">
      <h2>Player</h2>
      
      <div className="cards-container">
        {playerData.cards.map((card, index) => (
          inPlay ? (
            <Card key={index} card={card} />
          ) : null
        ))}
      </div>


      <div className="money">Money: ${playerData.money}</div>
      <div className="bet">Pot: ${playerData.bet * 2}</div>
      
      <div className="bet">
        <input 
          type="number" 
          value={betAmount} 
          onChange={(e) => setBetAmount(parseInt(e.target.value))} 
          placeholder="Enter bet amount" 
        />
        <button onClick={() => handleBet(betAmount)} disabled= {!playerData.player_in_game} >Bet</button>
      </div>
      <div className='button-container'>
        <button  onClick={() => handlePlayerAction('H')} disabled= {!playerData.player_in_game}>Hit</button>
        <button onClick={() => handlePlayerAction('S')} disabled= {!playerData.player_in_game}>Stand</button>

      </div>
      
    </div>
  );
};

export default Player;
