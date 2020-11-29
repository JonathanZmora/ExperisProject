from cardGame.Player import Player
from cardGame.DeckOfCards import DeckOfCards


class CardGame:

    def new_game(self):
        if not self.player1.pack == []:
            print("Error, the game has already started")
        else:
            self.deck.shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)

    def __init__(self, name1, name2, num_of_cards=10):
        self.deck = DeckOfCards()
        self.player1 = Player(name1, num_of_cards)
        self.player2 = Player(name2, num_of_cards)
        self.new_game()

    def get_winner(self):
        if len(self.player1.pack) > len(self.player2.pack):
            return self.player1.name
        elif len(self.player1.pack) < len(self.player2.pack):
            return self.player2.name
        else:
            return 'None'