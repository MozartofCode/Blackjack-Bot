import React, { useState, useEffect } from 'react';
import './styles/app.css';
import House from './components/House';
import Player from './components/Player';

import { fetchGameState } from './components/blackjackAPI';

const App = () => {
  const [house, setHouse] = useState({ money: 0, cards: [] });
  const [player, setPlayer] = useState({ money: 0, cards: [], cards2: [] });
  
 
  useEffect(() => {
    const initializeGame = async () => {
      const data = await fetchGameState();
      setHouse(data.house);
      setPlayer(data.player);
    };

    initializeGame();
  }, []);

  return (
    <div className="app-container">    
        <div className="players-container">
          <Player player={player} />

          <div className="bots">
            <House house={house} />
          </div>
        </div>
    </div>
  );
};

export default App;

