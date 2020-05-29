from IPython.display import clear_output
import random


def display_board(board):
    print('\n'*10)
    print(board[9] + ' | ' + board[8] + ' | ' + board[7])
    print(' ' + ' + ' + ' ' + ' + ' + ' ')
    print(board[6] + ' | ' + board[5] + ' | ' + board[4])
    print(' ' + ' + ' + ' ' + ' + ' + ' ')
    print(board[3] + ' | ' + board[2] + ' | ' + board[1])
    print('\n'*5)


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# display_board(board)


def player_input():
    '''
    OUTPUT = (player1 marker, player2 marker)
    '''
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O___').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


player_1_marker, player_2_marker = player_input()


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return((board[9] == board[8] == board[7] == mark) or
           (board[6] == board[5] == board[4] == mark) or
           (board[3] == board[2] == board[1] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[9] == board[5] == board[1] == mark) or
           (board[7] == board[5] == board[3] == mark))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
