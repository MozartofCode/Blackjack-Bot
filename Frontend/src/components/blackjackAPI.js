const API_BASE_URL = 'http://127.0.0.1:5000';


export const fetchGameState = async () => {
  const response = await fetch(`${API_BASE_URL}/game-state`);
  const data = await response.json();
  return data;
};

export const playerAction = async (action) => {
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


export const handlePlayerBet = async (bet) => {
    try {
        const response = await fetch(`${API_BASE_URL}/player-bet`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ bet }), 
        });
        if (!response.ok) {
            throw new Error(`Failed to perform player bet: ${bet}`);
        }
        const data = await response.json();
        return data
    } catch (error) {
        console.error(`Error performing player bet ${bet}:`, error);
    }
};