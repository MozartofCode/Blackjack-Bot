import React from 'react';
import Card from './Card';
import '../styles/house.css'


const House = ({ house }) => {
  
  const DownCardImage = require(`../down_card.png`);
  

  return (
    <div className="player-container">
      <h2>House</h2>
      <div className="cards-container">
      {house.cards.map((card, index) => (
          index === 0 ? (
            <div key={index} className="card">
              <img src= {DownCardImage} alt="Facedown card" />
            </div>
          ) : (
            <Card key={index} card={card} />
          )
        ))}
      </div>
      <div className="money">Money: ${house.money}</div>
    </div>
  );
};

export default House;
