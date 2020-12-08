from unittest import TestCase
from cardGame.Card import Card


class TestCard(TestCase):
    # If the init get corrrect values
    def test__init__working(self):
        card = Card(4, 2)
        self.assertTrue(card.value == 4 and card.suit == 2)
    # if the value out of range (1-14) raise error
    def test__init__value_not_in_range(self):
        with self.assertRaises(ValueError):
            Card(15, 2)
    # if the suit out of range (1-4) raise error
    def test__init__suit_not_in_range(self):
        with self.assertRaises(ValueError):
            Card(3, 5)
    # if the value = init raise error
    def test__init__value_not_int(self):
        with self.assertRaises(ValueError):
            Card('d', 4)
    # if the suit in the init != str raise error
    def test__init__suit_not_int(self):
        with self.assertRaises(ValueError):
            Card(3, 's')
    # if the suit and the value in the init != str raise error
    def test__init__both_params_not_int(self):
        with self.assertRaises(ValueError):
            Card('s', 'y')

