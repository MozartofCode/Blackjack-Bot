import React from 'react';
import Card from './Card';

const Bot4 = ({ bot4 }) => {
  return (
    <div className="player">
      <h2>Bot4</h2>
      <div className="cards">
        {bot4.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="Money">Money: {bot4.money}</div>
    </div>
  );
};

export default Bot4;