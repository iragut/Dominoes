import random

while True:
    domino_set = [[x, y] for x in range(7) for y in range(x, 7)]
    random.shuffle(domino_set)
    player_pieces = domino_set[:7]
    computer_pieces = domino_set[7:14]
    stock_pieces = domino_set[14:]
    domino_snake = []

    doubles = [piece for piece in player_pieces + computer_pieces if piece[0] == piece[1]]
    if len(doubles) == 0:
        continue
    highest_piece = max(doubles)

    if highest_piece in player_pieces:
        domino_snake.append(player_pieces.pop(player_pieces.index(highest_piece)))
        status = 'computer'
    else:
        domino_snake.append(computer_pieces.pop(computer_pieces.index(highest_piece)))
        status = 'player'
     
    print(f'Stock pieces: {stock_pieces}')
    print(f'Computer pieces: {computer_pieces}')
    print(f'Player pieces: {player_pieces}')
    print(f'Domino snake: {domino_snake}')
    print(f'Status: {status}')
    break
