from cardGame.DeckOfCards import DeckOfCards
from random import *


class Player:

    def __init__(self, name, num_of_cards=10):
        self.name = name
        if num_of_cards > 26:
            num_of_cards = 26
        self.num_of_cards = num_of_cards
        self.pack = []

    def set_hand(self, deck):
        deck.shuffle()
        for i in range(self.num_of_cards):
            self.pack += [deck.deal_one()]

    def get_card(self):
        index = randint(0, len(self.pack) - 1)
        card = self.pack[index]
        del self.pack[index]
        return card

    def add_card(self, card):
        self.pack.append(card)

    def show_player(self):
        print(f'name: {self.name}')
        for i in self.pack:
            print(i.print_card())
