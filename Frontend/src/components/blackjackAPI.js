const API_BASE_URL = 'http://127.0.0.1:5000';


export const fetchGameState = async () => {
  const response = await fetch(`${API_BASE_URL}/game-state`);
  const data = await response.json();
  return data;
};

export const playerAction = async (playerId, action) => {
  const response = await fetch(`${API_BASE_URL}/player-action`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ playerId, action }),
  });
  const data = await response.json();
  return data;
};
