from cardGame.CardGame import CardGame

card_game = CardGame('yoav', 'yonatan', 10)
card_game.player1.show()
card_game.player2.show()
for i in range(10):
    card1 = card_game.player1.get_card()
    card2 = card_game.player2.get_card()
    print(f'round {i + 1}:\n' + card_game.play_round(card1, card2) + '\n')
print('\nThe winner of the game is: ', card_game.get_winner())


