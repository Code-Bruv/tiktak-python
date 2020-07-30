# Global Variables


# board
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_', ]

# If game is still on
game_is_on = True

# Winner or Tie ?
winner = None

# Who's Turn
current_player = 'X'


# display board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# play game
def play_game():
    # Display initial board
    display_board()

    while game_is_on:
        # handle turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    if winner == 'X' or winner == '0':
        print(winner + ' WON :-)')
    elif winner == None:
        print('A TIE.')


# handle turn
def handle_turn(player):
    print(player + ' \'S TURN')
    position = input('CHOOSE POSITION FROM 1 TO 9 :')

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('INVALID INPUT.')

        position = int(position) - 1

        if board[position] == '_':
            valid = True
        else:
            print('FOLLOW THE RULES PUNK. WE DON\'T DO THAT HERE..:-(')

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


# check win
def check_if_win():
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_column()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # Setup global variables
    global game_is_on

    # check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'

    # If any rows does have a match, there is a win
    if row_1 or row_2 or row_3:
        game_is_on = False

    # Return the winner ( X or 0)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_column():
    # Setup global variables
    global game_is_on

    # check if any of the rows have all the same value
    column_1 = board[0] == board[3] == board[6] != '_'
    column_2 = board[1] == board[4] == board[7] != '_'
    column_3 = board[2] == board[5] == board[8] != '_'

    # If any rows does have a match, there is a win
    if column_1 or column_2 or column_3:
        game_is_on = False

    # Return the winner ( X or 0)
    if column_2:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]
    return


def check_diagonals():
    # Setup global variables
    global game_is_on

    # check if any of the rows have all the same value
    diagonal_1 = board[0] == board[4] == board[8] != '_'
    diagonal_2 = board[6] == board[4] == board[2] != '_'

    # If any rows does have a match, there is a win
    if diagonal_1 or diagonal_2:
        game_is_on = False

    # Return the winner ( X or 0)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


# check tie
def check_if_tie():
    global game_is_on
    if '_' not in board:
        game_is_on = False
    return


# flip player
def flip_player():
    global current_player

    # If the current Player was X,  then change it to 0
    if current_player == 'X':
        current_player = '0'

    # If the current Player was 0,  then change it to X
    elif current_player == '0':
        current_player = 'X'


play_game()
