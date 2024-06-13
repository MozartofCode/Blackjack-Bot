import React from 'react';
import Card from './Card';

const Bot2 = ({ bot2 }) => {
  return (
    <div className="player">
      <h2>Bot2</h2>
      <div className="cards">
        {bot2.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="Money">Money: {bot2.money}</div>
    </div>
  );
};

export default Bot2;