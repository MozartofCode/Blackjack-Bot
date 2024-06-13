import React from 'react';
import Card from './Card';

const Bot3 = ({ bot3 }) => {
  return (
    <div className="player">
      <h2>Bot3</h2>
      <div className="cards">
        {bot3.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="Money">Money: {bot3.money}</div>
    </div>
  );
};

export default Bot3;