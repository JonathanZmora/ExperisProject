from unittest import TestCase, mock
from cardGame.Player import Player
from cardGame.DeckOfCards import DeckOfCards
from cardGame.Card import Card


class TestPlayer(TestCase):

    def setUp(self):
        self.yonatan = Player('Yonatan')
        self.test_deck = DeckOfCards()

    def test__init__working(self):
        player = Player('yoav', 15)
        self.assertTrue(player.name == 'yoav' and player.num_of_cards == 15)

    def test__init__empty_name(self):
        with self.assertRaises(ValueError):
            Player('')

    def test__init__name_is_not_string(self):
        with self.assertRaises(ValueError):
            Player(4)

    def test__init__num_is_zero(self):
        with self.assertRaises(ValueError):
            Player('yoav', 0)

    def test__init__num_is_negative(self):
        with self.assertRaises(ValueError):
            Player('yoav', -1)

    def test__init__too_much_cards(self):
        player = Player('yoav', 30)
        self.assertTrue(player.num_of_cards == 26)

    @mock.patch('cardGame.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_got_enough_cards(self, mocked_deal_one):
        self.yonatan.set_hand(self.test_deck)
        self.assertEqual(len(self.yonatan.pack), 10)

    @mock.patch('cardGame.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_got_empty_deck(self, mocked_deal_one):
        self.test_deck = []
        with self.assertRaises(ValueError):
            self.yonatan.set_hand(self.test_deck)

    @mock.patch('cardGame.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_got_not_list(self, mocked_deal_one):
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
