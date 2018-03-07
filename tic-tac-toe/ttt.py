#!python
from IPython.display import clear_output
import sys
from random import *

next_player = {'X':'O', 'O':'X'}

def create_board():
    row = [' ']*3
    return [row, row.copy(), row.copy()]

def copy_board(board):
    new_board = []
    for r in board:
        new_board.append(r.copy())
    return new_board

def display_board(board):
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
    for r in board:
        if r[0] == r[1] == r[2] != ' ':
            return True
    for c in [0, 1, 2]:
        if board[0][c] == board[1][c] == board[2][c] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[2][0] == board[1][1] == board[0][2] != ' ':
        return True
    return False

def is_draw(board, player):
    if is_winner(board):
        return False
    player = next_player[player]
    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            if board[r][c] == ' ':
                new_board = copy_board(board)
                set_cell(new_board, player, (r,c))
                #display_board(new_board)
                if not is_draw(new_board, player):
                    return False;
    return True

def get_num(player):
    c = input(f"           Player {player} choose a cell (number 1-9, or q): ").lower()
    while not c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q']:
        c = input(f" Oops! Choose a cell (number 1-9, or q): ").lower()
    return c

def validate_cell(board, cell):
    return board[cell[0]][cell[1]] == ' '

def get_cell(board, player):
    num = get_num(player)
    while num != 'q':
        cell = [(2,0),(2,1),(2,2),
                (1,0),(1,1),(1,2),
                (0,0),(0,1),(0,2)][int(num)-1]
        if validate_cell(board, cell):
            return cell
        else:
            print("Oops: That cell is already taken")
    else:
        return 'q'

def set_cell(board, player, cell):
    board[cell[0]][cell[1]] = player
    return board

def play(player):
    board = create_board()
    display_board(board)
    quit = False
    while not quit:
        cell = get_cell(board, player)
        if cell == 'q':
            quit = True
            continue
        set_cell(board, player, cell)
        display_board(board)
        if is_winner(board):
            print(f"\n{player} is the Winner!")
            return
        elif is_draw(board, player):
            print("\nDraw")
            return
        player = next_player[player]
    else:
        print(f"\nPlayer {player} quit the game")

play_again = True
while play_again:
    player = sample(next_player.keys(), 1)[0]
    play(player)
    no_choice = True
    choice = ''
    while no_choice:
        choice = input("\nPlay again? ([y]/n): ")
        if not choice.lower() in ['y', '', 'n', 'q']:
            continue
        no_choice = False
    else:
        play_again = choice in ['y', '']
else:
    print("\nPlay again soon! Bye!")

