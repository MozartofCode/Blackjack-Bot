import React from 'react';

const GameControls = ({ gameState }) => {
  // Add additional game controls as needed
  return (
    <div className="game-controls">
      <button disabled={!gameState.canDeal}>Deal</button>
      <button disabled={!gameState.canReset}>Reset</button>
    </div>
  );
};

export default GameControls;
