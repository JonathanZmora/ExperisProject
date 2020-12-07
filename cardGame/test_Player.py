from unittest import TestCase
from cardGame.Player import Player
from cardGame.DeckOfCards import DeckOfCards
from cardGame.Card import Card


class TestPlayer(TestCase):

    def setUp(self):
        self.yonatan = Player('Yonatan')
        self.test_deck = DeckOfCards()

    def test_set_hand_got_enough_cards(self):
        self.yonatan.set_hand(self.test_deck)
        self.assertEqual(len(self.yonatan.pack), 10)

    def test_set_hand_got_empty_deck(self):
        self.test_deck = []
        with self.assertRaises(ValueError):
            self.yonatan.set_hand(self.test_deck)

    def test_set_hand_got_not_list(self):
        with self.assertRaises(ValueError):
            self.yonatan.set_hand(500)

    def test_get_card_delete_from_pack(self):
        self.yonatan.set_hand(self.test_deck)
        card = self.yonatan.get_card()
        self.assertNotIn(card, self.yonatan.pack)

    def test_get_card_returned(self):
        self.yonatan.set_hand(self.test_deck)
        card = self.yonatan.get_card()
        self.assertEqual(Card, type(card))

    def test_get_card_empty_pack(self):
        self.yonatan.pack = []
        with self.assertRaises(AttributeError):
            self.yonatan.get_card()

    def test_add_card_is_added(self):
        card = Card(10, 1)
        self.yonatan.add_card(card)
        self.assertIn(card, self.yonatan.pack)

    def test_add_card_got_not_card(self):
        with self.assertRaises(ValueError):
            self.yonatan.add_card('card')
