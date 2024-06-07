import random
import os

PLAYER_MARK = 'X'
COMPUTER_MARK = 'O'
AVAILABLE_MARK = ' '
GAMES_TO_MATCH = 5

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


def prompt(message):
    print(f'==> {message}')


def valid_selection(user_input):
    try:
        return 1 <= int(user_input) <= 9
    except ValueError:
        return False


def get_available_squares(board):
    return [square
            for square, value
            in board.items()
            if value == AVAILABLE_MARK]

# TODO - rename to marks square
def player_marks_square(board):
    available_squares = [str(square)
                         for square
                         in get_available_squares(board)]

    prompt(f'Choose a square : {join_or(available_squares)}')
    player_input = input().strip()

    while player_input not in available_squares:
        # We want to display custom error message based on the reason
        # why input is wrong
        if not valid_selection(player_input):
            msg = 'Invalid selection. Choose a square between 1 and 9'
        else:
            msg = (f'Square is already taken. Please select one of the '
                  f'available squares: {join_or(available_squares)}')

        prompt(msg)

        player_input = input().strip()

    board[int(player_input)] = PLAYER_MARK


def computer_marks_square(board):
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

# Check if anyone has all marks on the given line
def line_winner(board, line):
    if all([board[square] == PLAYER_MARK for square in line]):
        return 'player'
    if all([board[square] == COMPUTER_MARK for square in line]):
        return 'computer'

    return None


def get_game_winner(board):
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

def display_game_winner(winner):
    # TODO - refactor to game winner instead
    print('')
    if winner == 'computer':
        prompt("Computer wins the game. Better luck next time")
    else:
        prompt("You win the game! Nice!")

def display_tie():
    print('')
    prompt("It's a tie!")

def join_or(squares, separator = ', ', join_word = 'or'):
    if not squares:
        return ''
    if len(squares) == 1:
        return str(squares[0])
    if len(squares) == 2:
        return f' {join_word} '.join(
            [str(square) for square in squares])

    # Comprehension will return '{join word} {last_square}' for last square
    result = separator.join([
                str(square) if idx < (len(squares) - 1)
                else f'{join_word} ' + str(square)
                for idx, square in enumerate(squares)
            ])

    return result

def play_a_game():
    board = initialize_board()
    #  Keep playing until there's a winner or the board is full
    while True:
        display_board(board)
        player_marks_square(board)

        winner = get_game_winner(board)
        if winner or board_full(board):
            break

        computer_marks_square(board)

        winner = get_game_winner(board)
        if winner or board_full(board):
            break

    display_board(board)

    #  TODO - make sure to ask reviewer - is it better to do these displays in the main function
    if winner:
        display_game_winner(winner)
    else:
        display_tie()

    return winner

def display_match_winner(winner):
    if winner == 'computer':
        prompt("Computer wins the match. Better luck next time")
    else:
        prompt("You win the match! Congratulations!")

def display_current_scores(computer_score, player_score):
    prompt(f'Current Score. Player: {player_score} Game(s) '
           f'| Computer: {computer_score} Game(s)')


def display_welcome_message():
    clear_screen()
    prompt('Welcome to Tic-Tac-Toe! '
          f'Whoever wins {GAMES_TO_MATCH} games, wins the match.')
    input('Press Enter key to continue.\n')
    # prompt('Welcome to Tic-Tac-Toe!')

# Main game
def play_tic_tac_toe():
    computer_score = 0
    player_score = 0

    display_welcome_message()

    # Keep playing until player decides to stop
    while True:
        game_outcome = play_a_game()

        if game_outcome == 'computer':
            computer_score += 1
        elif game_outcome == 'player':
            player_score += 1
        
        display_current_scores(computer_score, player_score)
        
        if computer_score == GAMES_TO_MATCH or player_score == GAMES_TO_MATCH:
            display_match_winner(game_outcome)
            computer_score, player_score = 0, 0

        # Player can quit after any game,
        # even if the match is not over
        if not play_again():
            prompt('Goodbye then!')
            break


play_tic_tac_toe()