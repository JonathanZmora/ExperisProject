from cardGame.Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        self.deck = []
        for i in range(1, 14):
            self.deck += Card(i, "♦")

        for i in range(1, 14):
            self.deck += Card(i, "♠")

        for i in range(1, 14):
            self.deck += Card(i, "♥")

        for i in range(1, 14):
            self.deck += Card(i, "♣")

    def shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        index = randint(0, len(self.deck))
        card = self.deck[index]
        del self.deck[index]
        return card

    def show(self):
        for i in self.deck:
            i.__str__()