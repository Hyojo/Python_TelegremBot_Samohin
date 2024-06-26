def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    draw_board(board)
    player_one = input("Выберите х или о: ").lower()
    if player_one == "x":
        player_two = "o"
    else:
        player_two = "x"

    while True:
        ask_and_make_move(player_one, board)
        start_game = check_win(player_one, board)
        if not start_game:
            break

        ask_and_make_move(player_two, board)
        start_game = check_win(player_two, board)
        if not start_game:
            break


def draw_board(board):
    print("---+---+---")
    for i in range(3):
        print(" " + " | ".join(board[i]))
        print("---+---+---")


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(player, board, x, y)


def ask_move(player, board):
    x, y = input(f"Введите координаты своего хода '{player}'(x и y): ").split()
    x, y = int(x), int(y)
    if 0 <= x < 3 and 0 <= y < 3:
        return x, y
    else:
        print("Таких координат нет, попробуйте снова")
        ask_and_make_move(player, board)


def make_move(player, board, x, y):
    if board[x][y] == " ":
        board[x][y] = player
        draw_board(board)

    else:
        print("Клетка занята, попробуйте снова")
        ask_and_make_move(player, board)


def check_win(player, board):
    for i in range(3):
        if board[i].count(player) == len(board[i]):
            print(f"Выграли {player}")
            return False

        if board[0][i] == board[1][i] == board[2][i] == player:
            print(f"Выграли {player}")
            return False

    if board[0][0] == board[1][1] == board[2][2] == player:
        print(f"Выграли {player}")
        return False

    if board[0][2] == board[1][1] == board[2][0] == player:
        print(f"Выграли {player}")
        return False
    if not any(" " in x for x in board):
        print("Ничья")
        return False
    return True


tic_tac_toe()
