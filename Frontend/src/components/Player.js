import React from 'react';
import Card from './Card';
import '../styles/player.css'; 
import { playerAction, handlePlayerBet, fetchGameState } from './blackjackAPI';
import { useState, useEffect } from 'react';

const Player = ({ player }) => {
  const [playerData, setPlayerData] = useState(player);

  const handlePlayerAction = async (action) => {
    await playerAction(action);
    const updatedGameState = await fetchGameState();
    setPlayerData(updatedGameState.player);
  };


  return (
    <div className="player-container">
      <h2>Player</h2>
      
      <div className="cards-container">
        {player.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>

      <div className="money">Money: ${player.money}</div>
      <div className="bet">Bet: $0</div>

      <div className='button-container'>
        <button onClick={() => handlePlayerAction('H')}>Hit</button>
        <button onClick={() => handlePlayerAction('S')}>Stand</button>
      </div>
      
    </div>
  );
};

export default Player;
