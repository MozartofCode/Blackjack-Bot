import React from 'react';
import Card from './Card';

const Bot6 = ({ bot6 }) => {
  return (
    <div className="player">
      <h2>Bot6</h2>
      <div className="cards">
        {bot6.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="Money">Money: {bot6.money}</div>
    </div>
  );
};

export default Bot6;