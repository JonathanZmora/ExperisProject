from unittest import TestCase, mock
from cardGame.Player import Player
from cardGame.DeckOfCards import DeckOfCards
from cardGame.Card import Card


# unit tests for class Player functions
class TestPlayer(TestCase):
    # setUp function, builds a Player and a
    # deck of cards for use of the tests
    def setUp(self):
        self.yonatan = Player('Yonatan')  # PLayer
        self.test_deck = DeckOfCards()  # DeckOfCards

    # tests if the init function builds a Player
    # as it's supposed to when inserting valid parameters
    def test__init__working(self):
        player = Player('yoav', 15)  # builds a new Player with valid parameters
        # checks if the values were set to the attributes correctly
        self.assertTrue(player.name == 'yoav' and player.num_of_cards == 15)

    # tests the init function when an empty
    # string is inserted to parameter 'name'
    def test__init__empty_name(self):
        with self.assertRaises(ValueError):
            Player('')  # checks if the function raises an error when building this player

    # tests the init function when a non string
    # value is inserted to parameter 'name'
    def test__init__name_is_not_string(self):
        with self.assertRaises(ValueError):
            Player(4)  # checks if the function raises an error when building this player

    # tests the init function when the value zero
    # is inserted to parameter num_of_cards
    def test__init__num_is_zero(self):
        with self.assertRaises(ValueError):
            Player('yoav', 0)  # checks if the function raises an error when building this player

    # tests the init function when a negative value
    # is inserted to parameter num_of_cards
    def test__init__num_is_negative(self):
        with self.assertRaises(ValueError):
            Player('yoav', -1)  # checks if the function raises an error when building this player

    # tests the init function when a non int value
    # is inserted to parameter num_of_cards
    def test__init__num_not_int(self):
        with self.assertRaises(ValueError):
            Player('yoav', '1')  # checks if the function raises an error when building this player

    # tests the init function when a value
    # over 26 is inserted to parameter num_of_cards
    def test__init__too_much_cards(self):
        player = Player('yoav', 30)  # builds a player with the value 30 inserted into parameter num_of_cards
        self.assertTrue(player.num_of_cards == 26)  # checks if the function sets the value 26 to the attribute

    # tests if the set hand function deals the right amount of cards to the player
    # uses a mock object to mock the deal one function that set hand uses:
    # deal one will always return the same card with both attributes set to value 1
    @mock.patch('cardGame.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_got_enough_cards(self, mocked_deal_one):
        self.yonatan.set_hand(self.test_deck)  # player 'yonatan' uses the function set hand
        # 'yonatan's number of cards is the default 10, so this checks if he truly has 10 cards in hand:
        self.assertEqual(len(self.yonatan.pack), 10)

    # tests if the set hand inserts objects of class Card into the players list of cards
    # uses a mock object to mock the deal one function that set hand uses:
    # deal one will always return the same card with both attributes set to value 1
    @mock.patch('cardGame.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_deals_type_card(self, mocked_deal_one):
        self.yonatan.set_hand(self.test_deck)  # player 'yonatan' uses the function set hand
        condition = True  # a variable that will determine if the test will pass or fail.
        for i in self.yonatan.pack:  # for loop that runs on the players' cards in hand
            if not type(i) == Card:  # checks if the object in the current index is not of class Card
                condition = False  # if it's not the the variable is set to false and the test will fail
                break  # if the object is not break the loop because the test will fail
        self.assertTrue(condition)  # if the variable is true, the assert will pass, otherwise it will fail

    # tests if the set hand function gets an empty deck in the parameter
    # uses a mock object to mock the deal one function that set hand uses:
    # deal one will always return the same card with both attributes set to value 1
    @mock.patch('cardGame.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_got_empty_deck(self, mocked_deal_one):
        self.test_deck.deck = []  # sets the list of cards in the deck to an empty list
        with self.assertRaises(ValueError):
            self.yonatan.set_hand(self.test_deck)  # checks if an error is raised when using the function

    # tests if the set hand function gets a parameter value that is not a deck of cards
    # uses a mock object to mock the deal one function that set hand uses:
    # deal one will always return the same card with both attributes set to value 1
    @mock.patch('cardGame.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_got_not_deck(self, mocked_deal_one):
        with self.assertRaises(ValueError):
            self.yonatan.set_hand(500)  # in this case checks if an error is raised when parameter value is int

    # tests that the get card function deletes the card
    # thrown from the list of the cards in the players hand
    def test_get_card_delete_from_pack(self):
        self.yonatan.set_hand(self.test_deck)  # deals cards to the player
        card = self.yonatan.get_card()  # uses the function get card to get a card from the player into a variable
        self.assertNotIn(card, self.yonatan.pack)  # checks that this card no longer exists in the players hand

    # tests that the get card function returns an object of class Card
    def test_get_card_returned_card(self):
        self.yonatan.set_hand(self.test_deck)   # deals cards to the player
        card = self.yonatan.get_card()  # uses the function get card to get a card from the player into a variable
        self.assertEqual(Card, type(card))  # checks that the type of the variable is of class Card

    # tests the get card function when the player has no cards in hand
    def test_get_card_empty_pack(self):
        self.yonatan.pack = []  # sets the players hand to an empty hand
        with self.assertRaises(AttributeError):
            self.yonatan.get_card()  # checks if an error is raised when the function is used

    # test that the add card function does add the given card to the players hand
    def test_add_card_is_added(self):
        card = Card(10, 1)  # builds a card object
        self.yonatan.add_card(card)  # uses the add card function with the built card as the parameter
        self.assertIn(card, self.yonatan.pack)  # checks if the object is now in the players hand

    # tests the add card function when the parameter inserted is not of class Card
    def test_add_card_got_not_card(self):
        with self.assertRaises(ValueError):
            self.yonatan.add_card('card')  # checks if an error is raised when the function is used
