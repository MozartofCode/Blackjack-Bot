# @Author: Bertan Berker
# @Filename: Bot2.py
# Bot2 is an AI bot that makes decisions and bettings based on a neural network and the .csv dataset
# that I generated with the moves of bot1

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, Model
from sklearn.model_selection import train_test_split



class Bot2:
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.hand2 = []

    #TODO
    def play(self, input_data):
        return

    
    def hit(self, card):
        self.hand.append(card)
        
    def hit_2(self, card):
        self.hand2.append(card)

    def calculate_hand_val(self):
        return    
    






