from unittest import TestCase
from cardGame.CardGame import CardGame
from cardGame.Player import Player
from cardGame.Card import Card
from random import *
from cardGame.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck_test = DeckOfCards()

    def test_shuffle(self):
        list_of_cards = []
        for i in self.deck_test.deck:
            list_of_cards.append(i)
        shuffle(list_of_cards)
        self.assertListEqual(list_of_cards, self.deck_test.deck)

    def test_deal_one(self):
        list_1 = DeckOfCards()
        list_1.deal_one()
        self.assertEqual(len(list_1.deck), len(self.deck_test.deck) - 1)

    def test_show(self):
        pass
