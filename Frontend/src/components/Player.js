import React from 'react';
import Card from './Card';
import { handlePlayerAction } from './blackjackAPI';

const Player = ({ player }) => {
  

  return (
    <div className="player">
      <h2>Player {player.id}</h2>
      <div className="cards">
        {player.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="score">Score: {player.score}</div>
      <button onClick={() => handlePlayerAction('H')}>Hit</button>
      <button onClick={() => handlePlayerAction('S')}>Stand</button>
      <button onClick={() => handlePlayerAction('D')}>Double</button>
      <button onClick={() => handlePlayerAction('SP')}>Split</button>
      <button onClick={() => handlePlayerAction('SU')}>Surrender</button>
    </div>
  );
};

export default Player;
