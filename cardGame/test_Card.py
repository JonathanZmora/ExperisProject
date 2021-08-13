from unittest import TestCase
from cardGame.Card import Card


# unit tests for class Card functions
class TestCard(TestCase):

    # tests if the init function builds a Card object as it's supposed to
    # when inserting valid parameters
    def test__init__working(self):
        card = Card(4, 2)  # builds a card with valid parameters
        self.assertTrue(card.value == 4 and card.suit == 2)  # checks if the values where set to the attributes

    # tests the init function when the 'value' parameter inserted is not in range of 1 and 14
    def test__init__value_not_in_range(self):
        with self.assertRaises(ValueError):
            Card(15, 2)  # checks if the init function will raise an error when trying to build this Card

    # tests the init function when the 'suit' parameter inserted is not in range of 1 and 4
    def test__init__suit_not_in_range(self):
        with self.assertRaises(ValueError):
            Card(3, 5)  # checks if the init function will raise an error when trying to build this Card

    # tests the init function when the 'value' parameter inserted is not an integer
    def test__init__value_not_int(self):
        with self.assertRaises(ValueError):
            Card('d', 4)  # checks if the init function will raise an error when trying to build this Card

    # tests the init function when the 'suit' parameter inserted is not an integer
    def test__init__suit_not_int(self):
        with self.assertRaises(ValueError):
            Card(3, 's')  # checks if the init function will raise an error when trying to build this Card

    # tests the init function when both parameters inserted are not integers
    def test__init__both_params_not_int(self):
        with self.assertRaises(ValueError):
            Card('s', 'y')  # checks if the init function will raise an error when trying to build this Card

