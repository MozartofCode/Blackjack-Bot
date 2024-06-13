import React from 'react';
import Card from './Card';

const Bot1 = ({ bot1 }) => {
  return (
    <div className="player">
      <h2>Bot1</h2>
      <div className="cards">
        {bot1.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="Money">Money: {bot1.money}</div>
    </div>
  );
};

export default Bot1;
