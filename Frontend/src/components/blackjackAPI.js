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

export const handleBot2Play = async () => {
  try {
      const response = await fetch(`${API_BASE_URL}/bot2-action`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
      });
      if (!response.ok) {
          throw new Error('Failed to initiate bot2 play');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error initiating bot2 play:', error);
  }
};

export const handleBot3Play = async () => {
  try {
      const response = await fetch(`${API_BASE_URL}/bot3-action`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
      });
      if (!response.ok) {
          throw new Error('Failed to initiate bot3 play');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error initiating bot3 play:', error);
  }
};

export const handleBot4Play = async () => {
  try {
      const response = await fetch(`${API_BASE_URL}/bot4-action`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
      });
      if (!response.ok) {
          throw new Error('Failed to initiate bot4 play');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error initiating bot4 play:', error);
  }
};

export const handleBot5Play = async () => {
  try {
      const response = await fetch(`${API_BASE_URL}/bot5-action`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
      });
      if (!response.ok) {
          throw new Error('Failed to initiate bot5 play');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error initiating bot5 play:', error);
  }
};

export const handleBot6Play = async () => {
  try {
      const response = await fetch(`${API_BASE_URL}/bot6-action`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
      });
      if (!response.ok) {
          throw new Error('Failed to initiate bot6 play');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error initiating bot6 play:', error);
  }
};


export const handlePlayerAction = async (action) => {
    try {
        const response = await fetch(`${API_BASE_URL}/player-action`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action }), 
        });
        if (!response.ok) {
            throw new Error(`Failed to perform player action: ${action}`);
        }
        const data = await response.json();
        return data
    } catch (error) {
        console.error(`Error performing player action ${action}:`, error);
    }
};