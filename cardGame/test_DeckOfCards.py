from unittest import TestCase
from random import *
from cardGame.DeckOfCards import DeckOfCards
from cardGame.Card import Card


# unit tests for class DeckOfCards functions
class TestDeckOfCards(TestCase):
    # setUp function, builds a DeckOfCards object for use of the tests
    def setUp(self):
        self.deck_test = DeckOfCards()

    # tests if the init function builds a DeckOfCards object as it's supposed to
    # when inserting valid parameters
    def test__init__working(self):
        # checks if the length of list of Cards is 52, which means the list was built correctly
        # checks if the attribute type is in fact a list which means the deck of cards was built as requested
        self.assertTrue(len(self.deck_test.deck) == 52 and type(self.deck_test.deck) == list)

    # tests if the shuffle function does change the order of the objects in the deck
    def test_shuffle(self):
        list_of_cards = []  # builds an empty list
        for i in self.deck_test.deck:  # for loop that sets all Cards in the deck into the empty list
            list_of_cards.append(i)    # making it exactly the same as the deck
        self.deck_test.shuffle()  # shuffles the original deck
        # checks if the shuffled deck is not equal to the original deck using the eq function:
        self.assertTrue(not list_of_cards.__eq__(self.deck_test.deck))

    # test if the deal one function removes the card it dealt from the deck
    def test_deal_one_removes(self):
        new_deck = DeckOfCards()  # builds a new deck
        new_deck.deal_one()  # uses the function deal one to deal a card from the new deck
        # checks if the length of the new deck decreased by 1:
        self.assertEqual(len(new_deck.deck), len(self.deck_test.deck) - 1)

    # tests if the deal one function returns a Card object
    def test_deal_one_returns(self):
        res = self.deck_test.deal_one()  # uses the function deal on on a deck
        self.assertEqual(Card, type(res))  # checks if an object of class Card was returned

    # tests if the deal one function is used on an empty deck
    def test_deal_one_empty_deck(self):
        self.deck_test.deck = []  # sets the deck to an empty deck
        with self.assertRaises(AttributeError):
            self.deck_test.deal_one()  # checks if the use of the function raises an error

