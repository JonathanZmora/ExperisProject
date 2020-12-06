from unittest import TestCase
from cardGame.CardGame import CardGame
from cardGame.Player import Player
from cardGame.DeckOfCards import DeckOfCards
from cardGame.Card import Card


class TestCard(TestCase):

    def setUp(self):
        self.card1 = Card(10, 1)

    def test__str__(self):
        self.assertEqual('value: 10, suit: ♦', self.card1.__str__())

