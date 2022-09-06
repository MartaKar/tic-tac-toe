board = '|1|2|3|\n|4|5|6|\n|7|8|9|'
game_on = False
turns = 0
print(board)


def player_input():
    global turns
    global board
    turns += 1
    if turns % 2 == 0:
        player = input('Player 2, where do you want to put your symbol? ')
        check_input(player)
        board = board.replace(player, "O")
    else:
        player = input('Player 1, where do you want to put your symbol? ')
        check_input(player)
        board = board.replace(player, "X")
    print(board)
    return player


def check_for_win():
    if board[1] == board[3] == board[5] \
            or board[9] == board[11] == board[13] \
            or board[17] == board[19] == board[21]:
        return True
    elif board[1] == board[9] == board[17] \
            or board[3] == board[11] == board[19] \
            or board[5] == board[13] == board[21]:
        return True
    elif board[1] == board[11] == board[21] \
            or board[5] == board[11] == board[17]:
        return True


def check_input(player):
    try:
        x = int(player)
        spots = range(1, 10)
        if x not in spots:
            print("It's not a valid number")
    except ValueError:
        print("It's not a valid input")
    except None:
        print("It's not a valid input")




def game():
    global game_on
    game_on = True
    while game_on:
        player_input()
        if check_for_win():
            if turns % 2 == 0:
                print("You have won, Player 2")
            else:
                print("You have won, Player 1")
            game_on = False


game()
