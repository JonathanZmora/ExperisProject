from unittest import TestCase
from cardGame.CardGame import CardGame
from cardGame.Card import Card


# unit tests for class Player functions
class TestCardGame(TestCase):
    # setUp function, builds a card game object for use of the tests
    def setUp(self):
        self.game = CardGame('yonatan', 'yoav')

    # tests that the init function builds a CardGame object as it's supposed to
    def test__init__working(self):
        game = CardGame('yonatan', 'yoav', 15)  # builds a card game with valid parameters
        # checks if the player names were set to their attributes
        self.assertTrue(game.player1.name == 'yonatan' and game.player2.name == 'yoav')
        # checks if the num_of_cards parameter was set to its attribute
        self.assertTrue(game.player1.num_of_cards == 15 and game.player2.num_of_cards == 15)
        # checks if the init function deals the players the right amount of cards
        self.assertTrue(len(game.player1.pack) == 15 and len(game.player2.pack) == 15)
        # checks that after dealing the players their cards,
        # the deck of cards is left with the right amount of cards
        self.assertTrue(len(game.deck.deck) == 22)

    # tests the init function when the name1 parameter value is not a string
    def test__init__name1_is_not_string(self):
        with self.assertRaises(ValueError):
            CardGame(765, 'yoav', 15)  # checks if the function raises an error when building this CardGame

    # tests the init function when the name2 parameter value is not a string
    def test__init__name2_is_not_string(self):
        with self.assertRaises(ValueError):
            CardGame('yoav', 765, 15)  # checks if the function raises an error when building this CardGame

    # tests the init function when the name1 parameter value is an empty string
    def test__init__name1_is_empty(self):
        with self.assertRaises(ValueError):
            CardGame('', 'yoav', 15)  # checks if the function raises an error when building this CardGame

    # tests the init function when the name2 parameter value is an empty string
    def test__init__name2_is_empty(self):
        with self.assertRaises(ValueError):
            CardGame('yoav', '', 15)  # checks if the function raises an error when building this CardGame

    # tests the init function when the num_of_cards parameter value is zero
    def test__init__num_is_zero(self):
        with self.assertRaises(ValueError):
            CardGame('yoav', 'yonatan', 0)  # checks if the function raises an error when building this CardGame

    # tests the init function when the num_of_cards parameter value is negative
    def test__init__num_is_negative(self):
        with self.assertRaises(ValueError):
            CardGame('yoav', 'yonatan', -1)  # checks if the function raises an error when building this CardGame

    # tests the init function when the num_of_cards parameter value is not int
    def test__init__num_not_int(self):
        with self.assertRaises(ValueError):
            CardGame('yoav', 'yonatan', '1')  # checks if the function raises an error when building this CardGame

    # tests that when the new game function is used on a card game with
    # 2 players with empty hands it fills their hands with the right amount of cards
    def test_new_game_empty_pack(self):
        # checks if the amount of cards in player 1's hand is the default 10
        self.assertEqual(len(self.game.player1.pack), 10)
        # checks if the amount of cards in player 2's hand is the default 10
        self.assertEqual(len(self.game.player2.pack), 10)

    # tests that when the new game function is used on a card game where one
    # or both players have cards in their hands it doesn't deal them cards
    def test_new_game_not_empty(self):
        self.game.player1.pack = [Card(1, 1)]  # sets player 1's pack to one card in his hand
        self.game.new_game()  # uses the function new game
        # checks that the number of cards in player 1's hand is still 1:
        self.assertEqual(len(self.game.player1.pack), 1)

    # tests that the function get winner returns the right name when player 1 wins
    def test_get_winner_player_1(self):
        self.game.player1.pack.pop()  # removes a card from player 1's hand so he has less cards
        self.assertEqual(self.game.get_winner(), 'yonatan')  # checks if player 1 is the winner

    # tests that the function get winner returns the right name when player 2 wins
    def test_get_winner_player_2(self):
        self.game.player2.pack.pop()  # removes a card from player 2's hand so he has less cards
        self.assertEqual(self.game.get_winner(), 'yoav')  # checks if player 1 is the winner

    # tests that the function get winner returns 'None' when there is a draw
    def test_get_winner_draw(self):
        self.assertEqual(self.game.get_winner(), 'None')

    # tests that the play round function adds both
    # cards thrown in the round to the losing players hand
    def test_play_round_player1_value_greater(self):
        card1 = Card(10, 1)  # build card object 1 with greater value so it will win
        card2 = Card(8, 2)  # build card object 2 with smaller value so it will lose
        self.game.play_round(card1, card2)  # uses the play round function with the built cards
        # checks if both cards were added to player 2 who had the smaller value in his card
        self.assertTrue(card1 in self.game.player2.pack and card2 in self.game.player2.pack)

    def test_play_round_player2_value_greater(self):
        card1 = Card(8, 2)
        card2 = Card(10, 1)
        self.game.play_round(card1, card2)
        self.assertTrue(card1 in self.game.player1.pack and card2 in self.game.player1.pack)

    def test_play_round_player1_suit_greater(self):
        card1 = Card(10, 2)
        card2 = Card(10, 1)
        self.game.play_round(card1, card2)
        self.assertTrue(card1 in self.game.player2.pack and card2 in self.game.player2.pack)

    def test_play_round_player2_suit_greater(self):
        card1 = Card(10, 1)
        card2 = Card(10, 2)
        self.game.play_round(card1, card2)
        self.assertTrue(card1 in self.game.player1.pack and card2 in self.game.player1.pack)

    def test_play_round_card1_invalid_parameter1(self):
        with self.assertRaises(ValueError):
            self.game.play_round('card1', Card(1, 1))

    def test_play_round_card1_invalid_parameter2(self):
        with self.assertRaises(ValueError):
            self.game.play_round(Card(1, 1), 'card2')

    def test_play_round_card1_invalid_both_parameters(self):
        with self.assertRaises(ValueError):
            self.game.play_round('card1', 'card2')
