from cardGame.Player import Player
from cardGame.DeckOfCards import DeckOfCards


class CardGame:

    def new_game(self):
        if not self.player1.pack == [] or not self.player2.pack == []:
            print("Error, the game has already started")
        else:
            self.deck.shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)

    def __init__(self, name1, name2, num_of_cards=10):
        if type(name1) == str and type(name2) == str:
            if not name1 == '' and not name2 == '':
                if num_of_cards > 0:
                    self.deck = DeckOfCards()
                    self.player1 = Player(name1, num_of_cards)
                    self.player2 = Player(name2, num_of_cards)
                    self.new_game()
                else:
                    raise ValueError('the number of cards is less than 1')
            else:
                raise ValueError('one or both of the names is an empty string')
        else:
            raise ValueError('one or both of the names is not a string')

    def get_winner(self):
        if len(self.player1.pack) > len(self.player2.pack):
            return self.player2.name
        elif len(self.player1.pack) < len(self.player2.pack):
            return self.player1.name
        else:
            return 'None'

    def play_round(self, card1, card2):
        try:
            if card1.value > card2.value:
                self.player2.add_card(card1)
                self.player2.add_card(card2)
                str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player1.name}'
                return str1 + str2

            elif card2.value > card1.value:
                self.player1.add_card(card1)
                self.player1.add_card(card2)
                str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player2.name}'
                return str1 + str2
            else:
                if card1.suit > card2.suit:
                    self.player2.add_card(card1)
                    self.player2.add_card(card2)
                    str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                    str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player1.name}'
                    return str1 + str2

                else:
                    self.player1.add_card(card1)
                    self.player1.add_card(card2)
                    str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                    str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player2.name}'
                    return str1 + str2

        except:
            raise ValueError('one or both of the parameters where not of type Card')
