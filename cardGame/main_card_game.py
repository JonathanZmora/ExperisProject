from cardGame.CardGame import CardGame

card_game = CardGame('yoav', 'yonatan')
card_game.player1.show()
card_game.player2.show()
for i in range(11):
    card1 = card_game.player1.get_card()
    card2 = card_game.player1.get_card()
    if card1.value > card2.value:
        card_game.player2.add_card(card1)
        card_game.player2.add_card(card2)
        print(f'{card_game.player1.name} threw - {card1.__str__()}')
        print(f'{card_game.player2.name} threw - {card2.__str__()}')
        print('the winner is ', card_game.player1.name)

    elif card2.value > card1.value:
        card_game.player1.add_card(card1)
        card_game.player1.add_card(card2)
        print(f'{card_game.player1.name} threw - {card1.__str__()}')
        print(f'{card_game.player2.name} threw - {card2.__str__()}')
        print('the winner is ', card_game.player2.name)
    else:
        if card1.suit > card2.suit:
            card_game.player2.add_card(card1)
            card_game.player2.add_card(card2)
            print(f'{card_game.player1.name} threw - {card1.__str__()}')
            print(f'{card_game.player2.name} threw - {card2.__str__()}')
            print('the winner is ', card_game.player1.name)

        else:
            card_game.player1.add_card(card1)
            card_game.player1.add_card(card2)
            print(f'{card_game.player1.name} threw - {card1.__str__()}')
            print(f'{card_game.player2.name} threw - {card2.__str__()}')
            print('the winner is ', card_game.player2.name)

print('\nThe winner of the game is: ', card_game.get_winner())


