from random import *


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        print(f'value: {self.value}, suit: {self.suit}\n')


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
            self.pack[i] = deck.deal_one()

    def get_card(self):
        index = randint(0, len(self.pack) - 1)
        card = self.pack[index]
        del self.pack[index]
        return card

    def add_card(self, card):
        self.pack.append(card)

    def show(self):
        print(f'name: {self.name}')
        for i in self.pack:
            print(i.__str__())


class CardGame:

    def new_game(self):
        if not self.player1.pack == []:
            print("Error, the game has already started")
        else:
            self.deck.shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)

    def __init__(self, name1, name2, num_of_cards=10):
        self.deck = DeckOfCards()
        self.player1 = Player(name1, num_of_cards)
        self.player2 = Player(name2, num_of_cards)
        self.new_game()

    def get_winner(self):
        if len(self.player1.pack) > len(self.player2.pack):
            return self.player1.name
        elif len(self.player1.pack) < len(self.player2.pack):
            return self.player2.name
        else:
            return 'None'
