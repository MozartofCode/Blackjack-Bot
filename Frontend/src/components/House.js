import React from 'react';
import Card from './Card';

const House = ({ house }) => {
  return (
    <div className="player">
      <h2>House</h2>
      <div className="cards">
        {house.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="score">Score: {house.score}</div>
    </div>
  );
};

export default House;
