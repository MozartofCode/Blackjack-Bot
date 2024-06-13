import React, { useState, useEffect } from 'react';
import './styles/app.css';
import House from './components/House';
import Bot1 from './components/Bot1';
import Bot2 from './components/Bot2';
import Bot3 from './components/Bot3';
import Bot4 from './components/Bot4';
import Bot5 from './components/Bot5';
import Bot6 from './components/Bot6';
import Player from './components/Player';

import { fetchGameState } from './components/blackjackAPI';

const App = () => {
  const [house, setHouse] = useState({ money: 0, cards: [] });
  const [bot1, setBot1] = useState({ money: 0, cards: [] });
  const [bot2, setBot2] = useState({ money: 0, cards: [] });
  const [bot3, setBot3] = useState({ money: 0, cards: [] });
  const [bot4, setBot4] = useState({ money: 0, cards: [] });
  const [bot5, setBot5] = useState({ money: 0, cards: [] });
  const [bot6, setBot6] = useState({ money: 0, cards: [] });
  const [player, setPlayer] = useState({ money: 0, cards: [] });
  
 
  useEffect(() => {
    const initializeGame = async () => {
      const data = await fetchGameState();
      setHouse(data.house);
      setBot1(data.bot1);
      setBot2(data.bot2);
      setBot3(data.bot3);
      setBot4(data.bot4);
      setBot5(data.bot5);
      setBot6(data.bot6);
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
            <Bot1 bot1={bot1} />
            <Bot2 bot2={bot2} />
            <Bot3 bot3={bot3} />
            <Bot4 bot4={bot4} />
            <Bot5 bot5={bot5} />
            <Bot6 bot6={bot6} />
          </div>
        </div>
    </div>
  );
};

export default App;

