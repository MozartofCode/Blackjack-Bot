import React from 'react';
import PropTypes from 'prop-types';
import'../styles/card.css'

const Card = ({ card }) => {

  const formatCardName = (cardName) => {
    return cardName.replace(/\s/g, '_');
  };

  console.log(formatCardName(card))

  const formattedCardName = formatCardName(card);
  const cardImage = require(`../../Images/Cards/${formattedCardName}.png`);
  
  if (!cardImage) {
    console.error(`Image not found for card: ${formattedCardName}`);
    return null;
  }

  return (
    <div className="card">
      <img src={cardImage}/>
    </div>
  );
};

Card.propTypes = {
  card: PropTypes.string.isRequired,
};

export default Card;
