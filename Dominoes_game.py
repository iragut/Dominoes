import random

while True:
    domino_set = [[x, y] for x in range(7) for y in range(x, 7)]
    random.shuffle(domino_set)
    player_pieces = domino_set[:7]
    computer_pieces = domino_set[7:14]
    stock_pieces = domino_set[14:]
    domino_snake = []
    index = 0
    number = 1

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

    print("=" * 70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_pieces)}')
    print(f'''
{highest_piece}
''')

    while index < len(player_pieces):
        print(f"{number}:{player_pieces[index]}")
        index += 1
        number += 1

    print("")

    if status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")
    break
