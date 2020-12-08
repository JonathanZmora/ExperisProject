from unittest import TestCase
from cardGame.CardGame import CardGame
from cardGame.Card import Card


class TestCardGame(TestCase):

    def setUp(self):
        self.game = CardGame('yonatan', 'yoav')

    def test__init__working(self):     # check if the init work and get correct parameters

        game = CardGame('yonatan', 'yoav', 15)
        self.assertTrue(game.player1.name == 'yonatan' and game.player2.name)
        self.assertTrue(game.player1.num_of_cards == 15 and game.player2.num_of_cards == 15)
        self.assertTrue(len(game.player1.pack) == 15 and len(game.player2.pack) == 15)
        self.assertTrue(len(game.deck.deck) == 22)

    def test__init__name1_is_not_string(self):  # if name 1 !=  int raise error
        with self.assertRaises(ValueError):
            CardGame(765, 'yoav', 15)

    def test__init__name2_is_not_string(self):  # if name 2 !=  int raise error
        with self.assertRaises(ValueError):
            CardGame('yoav', 765, 15)

    def test__init__name1_is_empty(self):   # if name 1 empty raise error
        with self.assertRaises(ValueError):
            CardGame('', 'yoav', 15)

    def test__init__name2_is_empty(self):  # if name 2 empty raise error
        with self.assertRaises(ValueError):
            CardGame('yoav', '', 15)

    def test__init__num_is_zero(self):   # if number of cards = 0  raise error
        with self.assertRaises(ValueError):
            CardGame('yoav', 'yonatan', 0)

    def test__init__num_is_negative(self):   # if number of cards negative  raise error
        with self.assertRaises(ValueError):
            CardGame('yoav', 'yonatan', -1)

    def test__init__num_not_int(self):  # if number of cards != int raise error
        with self.assertRaises(ValueError):
            CardGame('yoav', 'yonatan', '1')

    def test_new_game_empty_pack(self):
        self.assertTrue(not self.game.player1.pack == [])
        self.assertTrue(not self.game.player2.pack == [])

    def test_new_game_not_empty(self):
        self.game.player1.pack = [Card(1, 1)]
        self.game.new_game()
        self.assertEqual(len(self.game.player1.pack), 1)

    def test_get_winner_player_1(self):   # test while the pack of player 1 smaller , player 1 winner
        self.game.player1.pack.pop()
        self.assertEqual(self.game.get_winner(), 'yonatan')

    def test_get_winner_player_2(self):  # test while the pack of player 2 smaller , player 2 winner
        self.game.player2.pack.pop()
        self.assertEqual(self.game.get_winner(), 'yoav')

    def test_get_winner_draw(self):  # test while the pack of player 1 equel to player 2 winner get "None"
        self.assertEqual(self.game.get_winner(), 'None')

    def test_play_round_player1_value_greater(self):
        card1 = Card(10, 1)
        card2 = Card(8, 2)
        self.game.play_round(card1, card2)
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
