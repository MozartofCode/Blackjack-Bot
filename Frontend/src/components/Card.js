import React from 'react';
import PropTypes from 'prop-types';

const Card = ({ card }) => {
  const cardImage = require(`../../Images/Cards/${card}.png`).default;

  return (
    <div className="card">
      <img src={cardImage} alt={card} />
    </div>
  );
};

Card.propTypes = {
  card: PropTypes.string.isRequired,
};

export default Card;
