from cardGame.DeckOfCards import DeckOfCards
from random import *
from cardGame.Card import Card


# a class that represents a single player in a game of cards
class Player:

    # constructor function, builds a player that has a name,
    # a number of cards he starts the game with,
    # and a list of cards that represents his cards in hand
    def __init__(self, name, num_of_cards=10):
        if type(name) == str:  # checks if the name is a string
            if not name == '':  # checks if parameter name is an empty string
                self.name = name
            else:
                raise ValueError('name')
        else:  # if the name is not string, raises an error
            raise ValueError('name parameter is not a string')
        if not type(num_of_cards) == int:  # checks if parameter num_of_cards is of type int
            raise ValueError('number of cards parameter value is not int')
        elif num_of_cards <= 0:  # checks if the number of cards is zero or negative
            raise ValueError('number of cards parameter value is less than 1')  # if it is, raises an error
        elif num_of_cards > 26:  # checks if the number of cards in more than the maximum of 26
            num_of_cards = 26  # if it is, sets it to 26
        self.num_of_cards = num_of_cards
        self.pack = []  # sets the player's list of cards in hand to an empty list(zero cards in hand)

    # set hand function, gets a deck of cards and deals cards to the players hand from the given deck
    # the number of cards dealt will be the number set to the attribute num_of_cards of the player
    def set_hand(self, deck):
        if not type(deck) == DeckOfCards:  # checks if the parameter type is not a deck of cards
            raise ValueError('the parameter is not a deck of cards')  # if not, raises an error
        elif not deck.deck:  # checks if the deck is not empty
            raise ValueError('the parameter deck is an empty deck')  # if not, raises an error
        else:  # if the parameter is a deck of cards and it is not empty:
            deck.shuffle()  # shuffles the deck
            for i in range(self.num_of_cards):  # for loop that runs in range of the number of cards to be dealt
                self.pack += [deck.deal_one()]  # deals a card from the deck and adds it to the players hand

    # get card function, returns and removes a random card from the players hand
    def get_card(self):
        if not len(self.pack) == 0:  # checks if the player doesn't have cards in his hand. if he does:
            index = randint(0, len(self.pack) - 1)  # picks a random index of a card
            card = self.pack[index]  # sets the card in that index to a variable "card"
            del self.pack[index]  # deletes the card from the list that holds the players cards
            return card  # returns the card
        else:  # if the player doesn't have cards in his hand, raises an error:
            raise AttributeError('the players pack is empty')

    # add card method, gets a parameter of class Card and adds it to the players hand
    def add_card(self, card):
        if type(card) == Card:  # checks if the parameter is of class Card
            self.pack.append(card)  # if it is, adds it to the list that holds the players cards
        else:  # if it is not, raises an error:
            raise ValueError('the parameter filled is not of type Card')

    # show function, prints all the players details:
    # the players name and description of his cards in hand using the Card class str function
    def show(self):
        print(f'player name: {self.name}\ncards in hand:')
        for i in self.pack:
            print(i.__str__())
        print()
