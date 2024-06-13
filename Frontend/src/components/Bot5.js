import React from 'react';
import Card from './Card';

const Bot5 = ({ bot5 }) => {
  return (
    <div className="player">
      <h2>Bot5</h2>
      <div className="cards">
        {bot5.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="Money">Money: {bot5.money}</div>
    </div>
  );
};

export default Bot5;