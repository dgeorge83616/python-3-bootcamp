'''
Tic-Tac-Toe Project
Dan George
'''
from random import sample
from IPython.display import clear_output

NEXT_PLAYER = {'X':'O', 'O':'X'}

def create_board():
    ''' Create a board '''
    row = [' ']*3
    return [row, row.copy(), row.copy()]

def copy_board(board):
    ''' Make a copy of the board '''
    new_board = []
    for row in board:
        new_board.append(row.copy())
    return new_board

def display_board(board):
    ''' Draw the board '''
    clear_output()
    print("")
    row = board[0]
    print(f" {row[0]} | {row[1]} | {row[2]} ")
    print(f"---+---+---")
    row = board[1]
    print(f" {row[0]} | {row[1]} | {row[2]} ")
    print(f"---+---+---")
    row = board[2]
    print(f" {row[0]} | {row[1]} | {row[2]} ")
    return board

def is_winner(board):
    ''' Check for winner '''
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for column in [0, 1, 2]:
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' \
            or board[2][0] == board[1][1] == board[0][2] != ' ':
        return True
    return False

def is_draw(board, a_player):
    ''' Determine if the move made by player has forced a draw '''
    if is_winner(board):
        return False
    a_player = NEXT_PLAYER[a_player]
    for row, _ in enumerate(board):
        for column, cell_value in row:
            if cell_value == ' ':
                new_board = copy_board(board)
                set_cell(new_board, a_player, (row, column))
                if not is_draw(new_board, a_player):
                    return False
    return True

def get_num(a_player):
    ''' Prompt the a_player until valid input '''
    char = input(f"          Player {a_player} choose a cell (number 1-9, or q): ").lower()
    while not char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q']:
        char = input(f" Oops! Choose a cell (number 1-9, or q): ").lower()
    return char

def validate_cell(board, cell):
    ''' Validates that the cell is not already taken '''
    return board[cell[0]][cell[1]] == ' '

def get_cell(board, a_player):
    '''
    Prompts the a_player for a cell and return it as a (x, y) tuple
    '''
    num = get_num(a_player)
    while num != 'q':
        cell = [(2, 0), (2, 1), (2, 2),
                (1, 0), (1, 1), (1, 2),
                (0, 0), (0, 1), (0, 2)][int(num)-1]
        if validate_cell(board, cell):
            return cell
        else:
            print("Oops: That cell is already taken")
    return 'q'

def set_cell(board, a_player, cell):
    '''
    Set the symbol passed in a_player into the cell argument
    '''
    board[cell[0]][cell[1]] = a_player
    return board

def play(n_player):
    '''
    Play a game using n_player arg as first mover
    '''
    board = create_board()
    display_board(board)
    while True:
        cell = get_cell(board, n_player)
        if cell == 'q':
            print(f"\nPlayer {n_player} quit the game")
            break
        set_cell(board, n_player, cell)
        display_board(board)
        if is_winner(board):
            print(f"\n{n_player} is the Winner!")
            return
        elif is_draw(board, n_player):
            print("\nDraw")
            return
        n_player = NEXT_PLAYER[n_player]

def session():
    ''' Runs games until players decided to stop playing '''
    play_again = True
    while play_again:
        player = sample(NEXT_PLAYER.keys(), 1)[0]
        play(player)
        no_choice = True
        choice = ''
        while no_choice:
            choice = input("\nPlay again? ([y]/n): ")
            if not choice.lower() in ['y', '', 'n', 'q']:
                continue
            no_choice = False
        play_again = choice in ['y', '']
    print("\nPlay again soon! Bye!")

session()
