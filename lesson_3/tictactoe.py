import random
import os

PLAYER_MARK = 'X'
COMPUTER_MARK = 'O'
AVAILABLE_MARK = ' '

def display_board(board):
    clear_screen()

    print('Reminder: Player: X, computer: O')
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')


def initialize_board():
    return {number: AVAILABLE_MARK for number in range(1,10)}
    # TESTING
    # return {number: PLAYER_MARK if number in [2,5,6,7,1] else ' ' for number in range(1,10)}


def prompt(message):
    print(f'==> {message}')


def valid_selection(user_input):
    try:
        return 1 <= int(user_input) <= 9
    except ValueError:
        return False


def get_available_squares(board):
    return [square for square, value in board.items() if value == AVAILABLE_MARK]


def player_makes_play(board):
    # TODO - maybe better to display the available options from the beginning, if some squares are taken 
    prompt('Choose a square between 1 and 9')
    player_input = input().strip()
    available_squares = get_available_squares(board)

    while player_input not in [str(square) for square in available_squares]:
        if not valid_selection(player_input):
            msg = 'Invalid selection. Choose a square between 1 and 9'
        else:
            msg = (f'Square is already taken. Please select one of the '
                  f'available squares: {available_squares}')
        
        prompt(msg)
        
        player_input = input().strip()
        
    board[int(player_input)] = PLAYER_MARK


def computer_makes_play(board):
    available_squares = get_available_squares(board)
    if available_squares:
        computer_selection = random.choice(available_squares)
        board[computer_selection] = COMPUTER_MARK


def play_again():
    print('')
    prompt('Play again? (y/n)')
    user_input = input().lower().strip()

    while user_input not in ['y', 'n', 'yes', 'no']:
        prompt('Invalid entry. Enter y/n:')
        user_input = input().lower().strip()
    
    return user_input[0] == 'y'


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def board_full(board):
    return len(get_available_squares(board)) == 0

def line_winner(board, line):
    # Player goes first so we first check if player won, then computer
    if all([board[square] == PLAYER_MARK for square in line]):
        return 'player'
    elif all([board[square] == COMPUTER_MARK for square in line]):
        return 'computer'
    else:
        return None


def get_winner(board):
    # Horizontal lines
    horizontal_lines = [
        [starting_square, starting_square + 1, starting_square + 2] 
        for starting_square in [1, 4, 7]
    ]
    vertical_lines = [
        [starting_square, starting_square + 3, starting_square + 6] 
        for starting_square in [1, 2, 3]
    ]
    diagonal_lines = [[1, 5, 9], [3, 5, 7]]

    winning_lines = horizontal_lines + vertical_lines + diagonal_lines

    for line in winning_lines:
        winner = line_winner(board, line)
        if winner:
            return winner

    # No winner found 
    return None

def display_winner(winner):
    print('')
    if winner == 'computer':
        prompt("Unfortunately, computer wins. Better luck next time")
    else:
        prompt("Congratulations! You win!")

def display_tie():
    print('')
    prompt("It's a tie!")

# Main game
def play_tic_tac_toe():
    while True:
        board = initialize_board()
        
        # Start of the round 
        while True:
            display_board(board)
            player_makes_play(board)

            winner = get_winner(board)
            if winner or board_full(board):
                break

            computer_makes_play(board)

            winner = get_winner(board)
            if winner or board_full(board):
                break

        display_board(board)

        if winner:
            display_winner(winner)
        else:
            display_tie()    

        if not play_again():
            prompt('Goodbye then!')
            break


play_tic_tac_toe()
