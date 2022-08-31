import random


def isint(num):  # check if input is an int
    try:
        int(num)
        return True
    except ValueError:
        return False


domino_set = [[x, y] for x in range(7) for y in range(x, 7)]  # create the set
random.shuffle(domino_set)

player_pieces = domino_set[:7]
computer_pieces = domino_set[7:14]
stock_pieces = domino_set[14:]

domino_snake = []

status = ""
highest_piece = 0

while True:
    doubles = [piece for piece in player_pieces + computer_pieces if piece[0] == piece[1]]  # find the biggest piece from a player
    if len(doubles) == 0:
        continue
    highest_piece = max(doubles)

    if highest_piece in player_pieces:
        domino_snake.append(player_pieces.pop(player_pieces.index(highest_piece)))
        status = 'computer'
        break
    else:
        domino_snake.append(computer_pieces.pop(computer_pieces.index(highest_piece)))
        status = 'player'
        break

the_game = [highest_piece]

while True:             # interface
    print("=" * 70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_pieces)}')

    if len(the_game) <= 6:
        the_game_string = [str(a) for a in the_game]
    else:
        the_game_string = [str(the_game[0]), str(the_game[1]), str(the_game[2]), "...", str(the_game[-3]), str(the_game[-2]), str(the_game[-1])]

    print(f'''
{"".join(the_game_string)}
''')

    index = 0
    number = 1

    print("Your pieces:")

    if len(player_pieces) == 0:           # win condition
        print("Status: The game is over. You won!")
        break
    elif len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        break

    while index < len(player_pieces):     # show player pieces
        print(f"{number}:{player_pieces[index]}")
        index += 1
        number += 1

    print("")

    if status == "computer":                 # computer player
        answer = input("Status: Computer is about to make a move. Press Enter to continue...\n")
        choice = random.randint(0, len(computer_pieces))

        if choice == 0:
            piece = random.choice(stock_pieces)
            computer_pieces.append(piece)
            stock_pieces.remove(piece)
            status = "player"

        else:
            piece = random.choice(computer_pieces)
            the_game.insert(-1, piece)
            computer_pieces.remove(piece)
            status = "player"

    else:                       # player
        answer = input("Status: It's your turn to make a move. Enter your command.\n")
        while True:
            if isint(answer) and -len(player_pieces) <= int(answer) <= len(player_pieces):
                if int(answer) > 0:
                    piece = player_pieces[int(answer) - 1]
                    the_game.append(piece)
                    player_pieces.remove(piece)
                    status = "computer"
                    break

                elif int(answer) < 0:
                    piece = player_pieces[abs(int(answer)) - 1]
                    the_game.insert(0, piece)
                    player_pieces.remove(piece)
                    status = "computer"
                    break

                else:
                    piece = random.choice(stock_pieces)
                    player_pieces.append(piece)
                    stock_pieces.remove(piece)
                    status = "computer"
                    break
            else:
                answer = input("Invalid input. Please try again.\n")

