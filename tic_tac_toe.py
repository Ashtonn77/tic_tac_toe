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


# get player marker
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


# tuple unpacking
#player_1_marker, player_2_marker = player_input()

# place choice on board


def place_marker(board, marker, position):
    board[position] = marker

# check for winner


def win_check(board, mark):
    return((board[9] == board[8] == board[7] == mark) or
           (board[6] == board[5] == board[4] == mark) or
           (board[3] == board[2] == board[1] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[9] == board[5] == board[1] == mark) or
           (board[7] == board[5] == board[3] == mark))

# which player goes first


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# check if board is empty at player selection


def space_check(board, position):

    return board[position] == ' '

# check if all spaces on board are filled


def full_board_check(board):

    for i in range(1, 10):
        if(space_check(board, i)):
            return False

    return True

# player choose place to place X OR O


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position : (1-9)  '))

    return position


# ask if player wants to play again
def replay():

    choice = input("Do you want to play again? Enter Yes or No  ")

    return choice == 'Yes'


# main
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' ']*10
    player_1_marker, player_2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n  ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player 1 Turn

            display_board(board)
            position = player_choice(board)
            place_marker(board, player_1_marker, position)

            if win_check(board, player_1_marker):
                display_board(board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(board)
            position = player_choice(board)
            place_marker(board, player_2_marker, position)

            if win_check(board, player_2_marker):
                display_board(board)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
