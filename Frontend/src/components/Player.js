import React from 'react';
import Card from './Card';
import '../styles/player.css'; 
import { handlePlayerAction } from './blackjackAPI';

const Player = ({ player }) => {
  

  return (
    <div className="player-container">
      <h2>Player</h2>
      <div className="cards-container">
        {player.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="money">Money: ${player.money}</div>

      <div className='button-container'>
        <button onClick={() => handlePlayerAction('H')}>Hit</button>
        <button onClick={() => handlePlayerAction('S')}>Stand</button>
        <button onClick={() => handlePlayerAction('D')}>Double</button>
        <button onClick={() => handlePlayerAction('SP')}>Split</button>
        <button onClick={() => handlePlayerAction('SU')}>Surrender</button>
      </div>
      
    </div>
  );
};

export default Player;
