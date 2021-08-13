# a class that represents a single card
class Card:
    # constructor function, builds a card object
    # gets the numeric value of the card and its suit
    # and places them in attributes value and suit
    def __init__(self, value, suit):
        if type(value) == int and type(suit) == int:  # checks if parameters are of type int
            if 0 < value < 15 and 0 < suit < 5:  # checks if the parameters are in the appropriate range
                self.value = value
                self.suit = suit
            else:  # if parameters are not in range, raises error
                raise ValueError('value not in range (1, 15) or suit not in range (1, 5)')
        else:  # if parameters are not int, raises error
            raise ValueError('value type or suit type is not int')

    # str function, returns card description:
    # the value and the suit of the card
    def __str__(self):

        # checks the suit number of the card
        # to determine which ascii character to print
        # 1 = diamond, 2 = spade, 3 = heart, 4 = club
        if self.suit == 1:
            return f'value: {self.value}, suit: ♦'
        elif self.suit == 2:
            return f'value: {self.value}, suit: ♠'
        elif self.suit == 3:
            return f'value: {self.value}, suit: ♥'
        else:
            return f'value: {self.value}, suit: ♣'
