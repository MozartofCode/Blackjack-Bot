
# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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

# Preprocess the data
def preprocess_data(df):
    num_cards = 52

    df['Player Hand'] = df['Player Hand'].apply(eval)
    df['Player Hand Encoded'] = df['Player Hand'].apply(lambda hand: [encode_card(card) for card in hand])
    df['House Upcard Encoded'] = df['House Upcard'].apply(encode_card)

    def one_hot_encode(cards, num_classes):
        encoding = np.zeros((num_classes,))
        for card in cards:
            encoding[card] = 1
        return encoding

    df['Player Hand One-Hot'] = df['Player Hand Encoded'].apply(lambda hand: one_hot_encode(hand, num_cards))
    df['House Upcard One-Hot'] = df['House Upcard Encoded'].apply(lambda card: one_hot_encode([card], num_cards))

    df['Input Features'] = df.apply(lambda row: np.concatenate([row['Player Hand One-Hot'], row['House Upcard One-Hot'], [row['Count']], [row['Bet']]]), axis=1)

    X = np.stack(df['Input Features'].values)
    y = df['Move'].values  # Assuming 'Move' is categorical

    return X, y

def create_random_forest_model():
    # Load the dataset
    df = pd.read_csv('blackjack_dataset.csv')
    X, y = preprocess_data(df)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    model_filepath = 'random_forest_model.pkl'
    joblib.dump(model, model_filepath)


# Function to make a prediction based on new input data
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

def predict_move(player_hand, house_upcard, count, bet, model):
    input_data = preprocess_input(player_hand, house_upcard, count, bet)
    move_prediction = model.predict(input_data)
    
    return move_prediction[0]

# Creating a random forest model
#create_random_forest_model()