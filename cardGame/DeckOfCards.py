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

    # deal one function, returns a random card from the deck
    # and takes the card out of the deck
    def deal_one(self):
        if not len(self.deck) == 0:  # checks if there are cards in the deck
            index = randint(0, len(self.deck) - 1)  # picks a random index in the list
            card = self.deck[index]  # saves the card in a variable
            del self.deck[index]  # deletes the card from the list
            return card  # returns the card
        else:  # if the deck is empty, raises an error:
            raise AttributeError('the deck is empty')

    # show function, returns the description of each card
    # in the deck using the Card class str function
    def show(self):
        for i in self.deck:  # for loop that runs on all of the cards in the deck
            i.__str__()  # calls for the Card class str function that returns its description
