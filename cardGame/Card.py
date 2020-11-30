# a class that represents a single card
class Card:
    # constructor function, builds a card object
    # gets the numeric value of the card and its suit
    # and places them in attributes value and suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

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
