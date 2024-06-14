import React from 'react';
import Card from './Card';
import '../styles/house.css'

const House = ({ house }) => {
  return (
    <div className="player-container">
      <h2>House</h2>
      <div className="cards-container">
        {house.cards.map((card, index) => (
          <Card key={index} card={card} />
        ))}
      </div>
      <div className="money">Money: ${house.money}</div>
    </div>
  );
};

export default House;
