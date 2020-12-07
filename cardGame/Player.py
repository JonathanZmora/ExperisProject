from cardGame.DeckOfCards import DeckOfCards
from random import *
from cardGame.Card import Card


class Player:

    def __init__(self, name, num_of_cards=10):
        if type(name) == str:
            self.name = name
        else:
            raise ValueError('Name parameter is not a string')
        if num_of_cards <= 0:
            raise ValueError('Name parameter is not a string')
        elif num_of_cards > 26:
            num_of_cards = 26
        self.num_of_cards = num_of_cards
        self.pack = []

    def set_hand(self, deck):
        if not type(deck) == DeckOfCards:
            raise ValueError('the parameter is not a deck of cards')
        elif not deck.deck:
            raise ValueError('the parameter deck is an empty deck')
        else:
            deck.shuffle()
            for i in range(self.num_of_cards):
                self.pack += [deck.deal_one()]

    def get_card(self):
        try:
            index = randint(0, len(self.pack) - 1)
            card = self.pack[index]
            del self.pack[index]
            return card
        except:
            raise AttributeError('the players pack is empty')

    def add_card(self, card):
        if type(card) == Card:
            self.pack.append(card)
        else:
            raise ValueError('the parameter filled is not of type Card')

    def show(self):
        print(f'player name: {self.name}\ncards in hand:')
        for i in self.pack:
            print(i.__str__())
        print()
