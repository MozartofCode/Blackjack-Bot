import React, { useState, useEffect } from 'react';
import './App.css';
import Player from './components/Player';
import House from './components/House';
import GameControls from './components/GameControls';
import { fetchGameState, playerAction } from './components/blackjackAPI';

const App = () => {
  const [house, setHouse] = useState({ score: 0, cards: [] });
  const [players, setPlayers] = useState([]);
  const [gameState, setGameState] = useState({});

  useEffect(() => {
    const initializeGame = async () => {
      const data = await fetchGameState();
      setHouse(data.house);
      setPlayers(data.players);
      setGameState(data.gameState);
    };

    initializeGame();
  }, []);

  const handlePlayerAction = async (playerId, action) => {
    const data = await playerAction(playerId, action);
    setHouse(data.house);
    setPlayers(data.players);
    setGameState(data.gameState);
  };

  return (
    <div className="game-container">
      <h1>Blackjack</h1>
      <House house={house} />
      <div className="players-container">
        {players.map((player) => (
          <Player key={player.id} player={player} onAction={handlePlayerAction} />
        ))}
      </div>
      <GameControls gameState={gameState} />
    </div>
  );
};

export default App;

