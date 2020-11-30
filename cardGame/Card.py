
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        if self.suit == 1:
            return f'value: {self.value}, suit: ♦'
        elif self.suit == 2:
            return f'value: {self.value}, suit: ♠'
        elif self.suit == 3:
            return f'value: {self.value}, suit: ♥'
        else:
            return f'value: {self.value}, suit: ♣'
