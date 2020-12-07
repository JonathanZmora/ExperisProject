from cardGame.Player import Player
from cardGame.DeckOfCards import DeckOfCards
from cardGame.Card import Card


# a class the represents a card game with two players
class CardGame:

    # new game function, starts a game of cards by dealing cards to the two players
    def new_game(self):
        if not self.player1.pack == [] or not self.player2.pack == []:  # checks if the players' hands are empty
            print("Error, the game has already started")  # if not, raises an error
        else:  # if they are empty:
            self.deck.shuffle()  # shuffles the deck
            self.player1.set_hand(self.deck)  # deals cards to player 1
            self.player2.set_hand(self.deck)  # deals cards to player 2

    # constructor function, builds a card game object
    # that consists of two players and a full deck of cards
    def __init__(self, name1, name2, num_of_cards=10):
        if type(name1) == str and type(name2) == str:  # checks that name parameters are string
            if not name1 == '' and not name2 == '':  # checks that name parameters are not empty strings
                if not type(num_of_cards) == int:  # checks that number of cards parameter is of type int
                    raise ValueError('the number of cards parameter is not int')  # if not, raises an error
                elif num_of_cards <= 0:  # checks if num_of_cards parameter value is zero or negative
                    raise ValueError('the number of cards parameter value is zero or negative')  # raises an error
                else:  # if all parameters are valid:
                    self.deck = DeckOfCards()  # builds a full deck of cards and sets it to attribute "deck"
                    self.player1 = Player(name1, num_of_cards)  # builds player 1
                    self.player2 = Player(name2, num_of_cards)  # builds player 2
                    self.new_game()  # starts the game by dealing cards to the players
            else:  # if one of the name parameters is an empty string, raises an error:
                raise ValueError('one or both of the names is an empty string')
        else:  # if one of the name parameters is not a string, raises an error:
            raise ValueError('one or both of the names is not a string')

    # get winner function, returns the name of the game winner
    # the winner is the player with less cards
    def get_winner(self):
        if len(self.player1.pack) > len(self.player2.pack):  # if player 1 has more cards:
            return self.player2.name  # returns player 2's name
        elif len(self.player1.pack) < len(self.player2.pack):  # if player 2 has more cards:
            return self.player1.name  # returns player 1's name
        else:  # if both players have the same number of cards in hand:
            return 'None'  # returns 'none'

    # play round function, gets two cards as parameters and plays a card game round:
    # each player throws a card, and the card with smaller value wins
    # the function adds both cards throw to the losing players hand
    # and returns a recap of the round: cards thrown and the winners name
    def play_round(self, card1, card2):
        if type(card1) == Card and type(card2) == Card:  # checks if the parameters are of class Card, if they are:
            if card1.value > card2.value:  # checks if the value of player 1's card is greater than player 2's
                self.player2.add_card(card1)  # if it is, add player 1's card to player 2's hand
                self.player2.add_card(card2)  # adds player 2's card to player 2's hand
                str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player1.name}'
                return str1 + str2  # returns the rounds recap

            elif card2.value > card1.value:  # checks if the value of player 2's card is greater than player 1's
                self.player1.add_card(card1)  # if it is, add player 1's card to player 1's hand
                self.player1.add_card(card2)  # adds player 2's card to player 1's hand
                str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player2.name}'
                return str1 + str2  # returns the rounds recap
            else:  # if both players' card values are the same:
                if card1.suit > card2.suit:  # checks if player 1's suit is greater than player 2's
                    self.player2.add_card(card1)  # if it is, add player 1's card to player 2's hand
                    self.player2.add_card(card2)  # adds player 2's card to player 2's hand
                    str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                    str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player1.name}'
                    return str1 + str2  # returns the rounds recap

                else:  # if player 2's suit is greater than player 1's:
                    self.player1.add_card(card1)  # add player 1's card to player 1's hand
                    self.player1.add_card(card2)  # add player 2's card to player 1's hand
                    str1 = f'{self.player1.name} threw - {card1.__str__()}\n'
                    str2 = f'{self.player2.name} threw - {card2.__str__()}\nthe winner is {self.player2.name}'
                    return str1 + str2  # returns the rounds recap

        else:  # if the parameters are not of class Card, raises an error:
            raise ValueError('one or both of the parameters where not of type Card')
