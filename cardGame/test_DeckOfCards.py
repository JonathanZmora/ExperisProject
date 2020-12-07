from unittest import TestCase
from random import *
from cardGame.DeckOfCards import DeckOfCards
from cardGame.Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck_test = DeckOfCards()

    def test_shuffle(self):
        list_of_cards = []
        for i in self.deck_test.deck:
            list_of_cards.append(i)
        shuffle(list_of_cards)
        self.assertListEqual(list_of_cards, self.deck_test.deck)

    def test_deal_one_removes(self):
        list_1 = DeckOfCards()
        list_1.deal_one()
        self.assertEqual(len(list_1.deck), len(self.deck_test.deck) - 1)

    def test_deal_one_returns(self):
        res = self.deck_test.deal_one()
        self.assertEqual(Card, type(res))

    def test_deal_one_empty_deck(self):
        self.deck_test.deck = []
        with self.assertRaises(AttributeError):
            self.deck_test.deal_one()

    def test_show(self):
        pass
