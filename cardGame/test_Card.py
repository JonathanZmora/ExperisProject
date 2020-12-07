from unittest import TestCase
from cardGame.Card import Card


class TestCard(TestCase):

    def test__init__valid_values(self):
        with self.assertRaises(ValueError):
            Card(4, 2)

    def test__init__value_not_in_range(self):
        with self.assertRaises(ValueError):
            Card(15, 2)

    def test__init__suit_not_in_range(self):
        with self.assertRaises(ValueError):
            Card(3, 5)

    def test__init__value_is_string(self):
        with self.assertRaises(ValueError):
            Card('d', 4)

    def test__init__suit_is_string(self):
        with self.assertRaises(ValueError):
            Card(3, 's')

    def test__init__both_params_string(self):
        with self.assertRaises(ValueError):
            Card('s', 'y')

    def test__init__working(self):
        card = Card(4, 2)
        self.assertTrue(card.value == 4 and card.suit == 2)
