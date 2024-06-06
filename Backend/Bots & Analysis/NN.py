# @Author: Bertan Berker
# @Filename: NN.py
# 
#
#

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, Model
from sklearn.model_selection import train_test_split

# Define a helper function to encode cards
def encode_card(card):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suit = card.split(' of ')[1]
    rank = card.split(' of ')[0]
    suit_idx = suits.index(suit)
    rank_idx = ranks.index(rank)
    return suit_idx * 13 + rank_idx

# Define a function to preprocess the input data
def preprocess_input(player_hand, house_upcard, count, bet):
    num_cards = 52
    player_hand_encoded = [encode_card(card) for card in player_hand]
    house_upcard_encoded = encode_card(house_upcard)

    def one_hot_encode(cards, num_classes):
        encoding = np.zeros((num_classes,))
        for card in cards:
            encoding[card] = 1
        return encoding

    player_hand_one_hot = one_hot_encode(player_hand_encoded, num_cards)
    house_upcard_one_hot = one_hot_encode([house_upcard_encoded], num_cards)

    input_features = np.concatenate([player_hand_one_hot, house_upcard_one_hot, [count], [bet]])
    return input_features.reshape(1, -1)


def create_NN_model(filename, output_model_name):
    # Normalize and one-hot encode the cards
    num_cards = 52
    def one_hot_encode(cards, num_classes):
        encoding = np.zeros((num_classes,))
        for card in cards:
            encoding[card] = 1
        return encoding


    # Load the dataset
    df = pd.read_csv(filename)

    # Encode player hand and house upcard
    df['Player Hand'] = df['Player Hand'].apply(eval)
    df['Player Hand Encoded'] = df['Player Hand'].apply(lambda hand: [encode_card(card) for card in hand])
    df['House Upcard Encoded'] = df['House Upcard'].apply(encode_card)
    df['Player Hand One-Hot'] = df['Player Hand Encoded'].apply(lambda hand: one_hot_encode(hand, num_cards))
    df['House Upcard One-Hot'] = df['House Upcard Encoded'].apply(lambda card: one_hot_encode([card], num_cards))

    # Combine features into a single input vector
    df['Input Features'] = df.apply(lambda row: np.concatenate([row['Player Hand One-Hot'], row['House Upcard One-Hot'], [row['Count']], [row['Bet']]]), axis=1)

    unique_moves = df['Move'].nunique()

    # Define the input shape
    input_shape = df['Input Features'].iloc[0].shape

    # Define the model
    inputs = layers.Input(shape=input_shape)
    x = layers.Dense(128, activation='relu')(inputs)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dense(32, activation='relu')(x)

    # Output for move prediction
    move_output = layers.Dense(unique_moves, activation='softmax', name='move_output')(x)

    # Combine the model
    model = Model(inputs=inputs, outputs=move_output)

    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    # Convert input features and targets to numpy arrays
    X = np.stack(df['Input Features'].values)
    y_move = pd.get_dummies(df['Move']).values  # Assuming 'Move' is categorical

    # Split the data
    X_train, X_test, y_move_train, y_move_test = train_test_split(X, y_move, test_size=0.2, random_state=42)
    model.fit(X_train, y_move_train, epochs=50, validation_split=0.2)

    model_path = output_model_name
    model.save(model_path)


# Function to make a prediction based on new input data
def predict_move(player_hand, house_upcard, count, bet, model, df):
    input_data = preprocess_input(player_hand, house_upcard, count, bet)
    move_prediction = model.predict(input_data)
    move_index = np.argmax(move_prediction)
    
    # Assuming you have a mapping of move index to move label
    move_label_mapping = {index: label for index, label in enumerate(df['Move'].unique())}
    predicted_move = move_label_mapping[move_index]
    
    return predicted_move


# Used this initially for creating the models
#create_NN_model("blackjack_dataset.csv", "blackjack_model_bot2.h5")
#create_NN_model("blackjack_dataset_player.csv", "blackjack_model_player.h5")
