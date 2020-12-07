from cardGame.Card import Card
from random import *


# a class that represents a full
# deck of cards as a list
class DeckOfCards:

    # constructor function, builds a full deck of 52 cards
    # creates a list named 'deck' and adds all the cards into it
    def __init__(self):
        self.deck = []  # creation of list named 'deck'
        for i in range(1, 14):  # loop for adding diamond suit
            self.deck += [Card(i, 1)]

        for i in range(1, 14):  # loop for adding spade suit
            self.deck += [Card(i, 2)]

        for i in range(1, 14):  # loop for adding heart suit
            self.deck += [Card(i, 3)]

        for i in range(1, 14):  # loop for adding club suit
            self.deck += [Card(i, 4)]

    # shuffle function, shuffles the cards
    # in the deck to a random order
    def shuffle(self):
        shuffle(self.deck)  # a python function, gets a list and shuffles the values

    def deal_one(self):
        try:
            index = randint(0, len(self.deck) - 1)
            card = self.deck[index]
            del self.deck[index]
            return card
        except:
            raise AttributeError('the deck is empty')



    def show(self):
        for i in self.deck:
            i.__str__()