from cardGame.CardGame import CardGame

card_game = CardGame('yoav', 'yonatan')
card_game.player1.show()
card_game.player2.show()
for i in range(10):
    print(f'round {i + 1}:\n' + card_game.play_round() + '\n')
print('\nThe winner of the game is: ', card_game.get_winner())


