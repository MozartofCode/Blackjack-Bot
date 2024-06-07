# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Define a helper function to encode cards
def encode_card(card):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suit = card.split(' of ')[1]
    rank = card.split(' of ')[0]
    suit_idx = suits.index(suit)
    rank_idx = ranks.index(rank)
    return suit_idx * 13 + rank_idx


def create_decision_tree_model():

    # Load the dataset
    df = pd.read_csv('blackjack_dataset_player.csv')

    # Preprocess the data
    df['Player Hand'] = df['Player Hand'].apply(eval)
    df['Player Hand Encoded'] = df['Player Hand'].apply(lambda hand: [encode_card(card) for card in hand])
    df['House Upcard Encoded'] = df['House Upcard'].apply(encode_card)

    # Normalize and one-hot encode the cards
    num_cards = 52
    def one_hot_encode(cards, num_classes):
        encoding = np.zeros((num_classes,))
        for card in cards:
            encoding[card] = 1
        return encoding

    df['Player Hand One-Hot'] = df['Player Hand Encoded'].apply(lambda hand: one_hot_encode(hand, num_cards))
    df['House Upcard One-Hot'] = df['House Upcard Encoded'].apply(lambda card: one_hot_encode([card], num_cards))

    # Combine features into a single input vector
    df['Input Features'] = df.apply(lambda row: np.concatenate([row['Player Hand One-Hot'], row['House Upcard One-Hot'], [row['Count']], [row['Bet']]]), axis=1)

    # Convert input features and targets to numpy arrays
    X = np.stack(df['Input Features'].values)
    y = df['Move']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the decision tree model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Test accuracy: {accuracy}")

    # Save the model
    joblib.dump(model, 'decision_tree_model.joblib')

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

# Function to make a prediction based on new input data
def predict_move(player_hand, house_upcard, count, bet, model):
    input_data = preprocess_input(player_hand, house_upcard, count, bet)
    move_prediction = model.predict(input_data)
    return move_prediction[0]

# Creating a model
# create_decision_tree_model()