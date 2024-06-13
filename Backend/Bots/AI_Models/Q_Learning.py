# @Author: Bertan Berker
# @Filename: Q_Learning.py
# This is a reinforcement learning (Q-Learning) based bot where the bot has only hit or stand functionality
# https://www.gymlibrary.dev/environments/toy_text/blackjack/

import numpy as np
import random
import gym

env = gym.make('Blackjack-v1')

observation_space_size = (32, 11, 2)  # Example: player hand sum (0-31), dealer's upcard (1-10), usable ace (0 or 1)

# Hit or stick so action space size is 2
action_space_size = 2

# Initialize Q-table with zeros
q_table = np.zeros(observation_space_size + (action_space_size,))

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_decay = 0.995
min_epsilon = 0.01
total_episodes = 100000  # Number of training episodes

# Helper function to encode state
def encode_state(observation):
    player_sum, dealer_card, usable_ace = observation
    return player_sum, dealer_card, int(usable_ace)


# Training loop
for episode in range(total_episodes):
    observation, info = env.reset()
    state = encode_state(observation)
    done = False

    while not done:
        # Exploration-exploitation trade-off
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Explore: choose a random action
        else:
            action = np.argmax(q_table[state])  # Exploit: choose the action with max value (Q-value)

        next_observation, reward, done, info, dictionary = env.step(action)
        next_state = encode_state(next_observation)

        # Q-value update
        q_table[state + (action,)] = q_table[state + (action,)] + alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state + (action,)]
        )

        state = next_state

    # Decay epsilon
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

# Save the trained Q-table for future use
# np.save('q_table_blackjack.npy', q_table)

# Function to make a move prediction based on the learned Q-table
def predict_move(observation, q_table):
    state = encode_state(observation)
    return np.argmax(q_table[state])
    
    