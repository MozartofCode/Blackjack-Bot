const API_BASE_URL = 'http://127.0.0.1:5000';


export const fetchGameState = async () => {
  const response = await fetch(`${API_BASE_URL}/game-state`);
  const data = await response.json();
  return data;
};

export const handleBot1Play = async () => {
  try {
      const response = await fetch(`${API_BASE_URL}/bot1-action`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
      });
      if (!response.ok) {
          throw new Error('Failed to initiate bot1 play');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error initiating bot1 play:', error);
  }
};