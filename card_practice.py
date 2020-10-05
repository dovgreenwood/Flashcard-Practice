"""
@author Dov Greenwood
@date October 2, 2020

The goal of my card practicing program is to use logistic regression to study flashcards.
Essentially, it will work as follows:
    Each card can be rated in terms of confidence on a scale of 1-5 during practice.
    Regression will be used to measure *true* confidence, by tracking whether your confidence in a given card is waxing
    or waning across that past ~20 times you've seen the card.
    It then shows you cards with frequency based on your true confidence rather than your psychological confidence.

The following objects and functions must be implemented:
class card_storage:
    - reads a flashcards csv into a dataframe
    - modifies the list of 20 past confidence ratings
    - adds a true_confidence column to the dataframe, and re-evaluates the true_confidence whenever the card is tested
    - writes the dataframe back into the flashcards csv
def true_confidence:
    - takes a entry from confidence_20
    - returns the slope and intercept (or whatever coefficients are relevant) of the "true" confidence
def card_order:
    - takes a single column dataframe containing true_confidence, and an integer num_lowest containing the number of lowest rated card indices to return
    - returns a list of indices in order of which to test
def test_round:
    - takes a card_order, card_storage, and integer of num_cards to test this round
    - re-evaluates card_order
    - selects at random num_cards from card_order and shuffles the indices
    - tests on the selected cards from card_storage
    - feeds card_storage the new confidence values
"""

import numpy as np
import pandas as pd
from scipy import stats as st
import random

def true_confidence(card_confidence):
    #fits line as f(attempt_number) = confidence(attempt_number)
    #NOTE TO SELF: intercept > 5 is BAD, since the only way this could happen is on a decline. Need to find a way to balance slope and intercept in deciding "confidence."
    #use logistic regression
    attempts = [i+1 for i in range(20)]
    r_line = st.linregress(attempts, card_confidence)
    return (r_line[0], r_line[1]) #(slope, intercept)

def card_order(true_confidence, num_lowest):
    tc_with_index = [(true_confidence[i][0], true_confidence[i][1], i) for i in range(len(true_confidence))]
    tc_ordered = np.array(sorted(tc_with_index))
    return tc_ordered[:num_lowest, 2]
    #confidence_ordered = np.array(true_confidence)
    #confidence_ordered = np.sort(confidence_ordered)

def test_round(card_storage, num_cards):
    indices = card_order(card_storage.get_true_confidence(), num_cards * 2)
    indices_for_round = random.choices(indices, k=num_cards)
    #TEST ON THESE CARDS

class card_reader:
    def __init__(self, flashcards):
        """
        Parameters:
            flashcards: a csv file containing the following columns:
                front_side: str
                    the front side of the flashcard
                back_side: str
                    the back side of the flashcard
                confidence_20: list
                    the past 20 confidence ratings for each card, on a scale of 1-5
        """
        self.cards = pd.read_csv(flashcards)
        self.cards['true_confidence'] = [(0,0) for i in range(len(self.cards))]
        for i in range(len(self.cards)):
            self.cards.iloc[i]['true_confidence'] = true_confidence(self.cards.iloc[i]['confidence_20'])

    def get_true_confidence(self):
        return self.cards['true_confidence']

    def update_confidence(self, index, rating):
        self.cards.confidence_20[index] = self.cards.iloc[index]['confidence_20'][1:20]
        self.cards.confidence_20[index].append(rating)
        self.cards.iloc[index]['true_confidence'] = true_confidence(self.cards.iloc[i]['confidence_20'])

    def write_card_data(self, file_path):
        return
