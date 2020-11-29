from random import *


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        print('value: ' + str(self.value) + ', suit: ' + str(self.suit))
