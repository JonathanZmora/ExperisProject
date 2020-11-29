from random import *


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        print(f'value: {self.value}, suit: {self.suit}\n')
