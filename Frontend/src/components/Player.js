import React from 'react';
import Card from './Card';

const Player = ({ player, onAction }) => {
  const handleAction = (action) => {
    onAction(player.id, action);
  };

  return (
    <div className="player">
      <h2>Player {player.id}</h2>
      <div className="cards">
        {player.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="score">Score: {player.score}</div>
      <button onClick={() => handleAction('hit')}>Hit</button>
      <button onClick={() => handleAction('stand')}>Stand</button>
      <button onClick={() => handleAction('double')}>Double</button>
      <button onClick={() => handleAction('split')}>Split</button>
      <button onClick={() => handleAction('surrender')}>Surrender</button>
    </div>
  );
};

export default Player;
