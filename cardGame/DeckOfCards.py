from cardGame.Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        self.deck = []
        for i in range(1, 14):
            self.deck += [Card(i, 1)]

        for i in range(1, 14):
            self.deck += [Card(i, 2)]

        for i in range(1, 14):
            self.deck += [Card(i, 3)]

        for i in range(1, 14):
            self.deck += [Card(i, 4)]

    def shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        index = randint(0, len(self.deck) - 1)
        card = self.deck[index]
        del self.deck[index]
        return card

    def show(self):
        for i in self.deck:
            i.__str__()