import random
import os
import sys

PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
AVAILABLE_MARKER = ' '
OPTIMAL_SQUARE = 5
GAME_START = 'choose'


def display_board(board, current_scores):
    clear_screen()

    display_prompt('Player: X, computer: O')
    display_current_scores(current_scores)

    print('')
    print('1    |2    |3')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('4    |5    |6')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('7    |8    |9')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')


def display_match_winner(winner):
    if winner == 'computer':
        display_prompt("Computer wins the game and the match! "
                       "Better luck next time")
    else:
        display_prompt("You win the game and the match! Congratulations!")


def display_current_scores(scores):
    display_prompt(f'Current Score. Player: {scores['player']} Game(s) '
           f'| Computer: {scores['computer']} Game(s)')


def display_welcome_message():
    clear_screen()
    display_prompt('Welcome to Tic-Tac-Toe!')


def display_game_outcome(outcome):
    print('')
    match outcome:
        case 'computer':
            display_prompt("Computer wins the game. Better luck next time")
        case 'player':
            display_prompt("You win the game! Nice!")
        case 'tie':
            display_prompt("It's a tie!")


def display_prompt(message):
    print(f'==> {message}')


def get_available_squares(board):
    return [square
            for square, value
            in board.items()
            if value == AVAILABLE_MARKER]


def get_winning_lines():
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

    return winning_lines


def get_strategic_square(line, board, strategy):
    # Depending on strategy we're checking if
    # 2 squares in a row are marked by player or computer
    if strategy == 'defense':
        marker_to_check = PLAYER_MARKER
    elif strategy in ('offense','potential_win'):
        marker_to_check = COMPUTER_MARKER

    markers_in_line = [ board[square] for square in line ]

    if markers_in_line.count(marker_to_check) == 2:
        for square in line:
            if board[square] == AVAILABLE_MARKER:
                return square

    #  Potential win: a line with
    # 1 computer marker and no player markers
    if strategy == 'potential_win':
        if (markers_in_line.count(COMPUTER_MARKER) == 1
            and markers_in_line.count(PLAYER_MARKER) == 0):
            for square in line:
                if board[square] == AVAILABLE_MARKER:
                    return square

    return None


# Check if anyone has all marks on the given line
def get_line_winner(board, line):
    if all([board[square] == PLAYER_MARKER for square in line]):
        return 'player'
    if all([board[square] == COMPUTER_MARKER for square in line]):
        return 'computer'

    return None


def get_game_winner(board):
    for line in get_winning_lines():
        winner = get_line_winner(board, line)
        if winner:
            return winner

    # No winner found
    return None


def get_formatted_squares_options(squares, separator = ', ', join_word = 'or'):
    if not squares:
        return ''
    if len(squares) == 1:
        return str(squares[0])
    if len(squares) == 2:
        return f' {join_word} '.join(
            [str(square) for square in squares])

    # Comprehension will return '{join word} {last_square}' for the
    # last square
    result = separator.join([
                str(square) if idx < (len(squares) - 1)
                else f'{join_word} ' + str(square)
                for idx, square in enumerate(squares)
            ])

    return result


def get_alternate_player(current_player):
    return 'computer' if current_player == 'player' else 'player'


def prompt_play_again():
    print('')
    display_prompt('Play another match? (y/n)')
    user_input = input().lower().strip()

    while user_input not in ['y', 'n', 'yes', 'no']:
        display_prompt('Invalid entry. Enter y/n:')
        user_input = input().lower().strip()

    return user_input[0] == 'y'

def prompt_to_continue():
    display_prompt('Press enter to continue')
    input()


def prompt_games_to_match_number():
    display_prompt('How many games to win a match? Enter a number:')
    games_to_match_input = input()
    while not valid_games_number(games_to_match_input):
        display_prompt('Invalid entry. Enter a positive number:')
        games_to_match_input = input()

    return int(games_to_match_input)


def prompt_game_start_selection():
    display_prompt('Who will start? Enter 1 for player, 2 for computer')
    game_start_selection = input().strip()
    while game_start_selection not in ['1','2']:
        display_prompt('Enter 1 for player, 2 for computer')
        game_start_selection = input().strip()

    return 'player' if game_start_selection == '1' else 'computer'


def board_full(board):
    return len(get_available_squares(board)) == 0


def valid_games_number(user_input):
    try:
        games_number = int(user_input)
        return games_number > 0
    except ValueError:
        return False


def valid_square_selection(user_input):
    try:
        return 1 <= int(user_input) <= 9
    except ValueError:
        return False


def initialize_board():
    return {number: AVAILABLE_MARKER for number in range(1,10)}


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def player_marks_square(board):
    available_squares = [str(square)
                         for square
                         in get_available_squares(board)]

    display_prompt(
        f'Choose a square : '
        f'{get_formatted_squares_options(available_squares)}'
        "\nor q to quit"
    )

    player_input = input().strip()

    while player_input not in available_squares and player_input != 'q':
        # We want to display custom error message based on the reason
        # why input is wrong
        if not valid_square_selection(player_input):
            msg = ('Invalid selection. Choose a square between 1 and 9'
                   ' \nor q to quit')
        else:
            msg = (f'Square is already taken. Please select one of the '
                  f'available squares: '
                  f'{get_formatted_squares_options(available_squares)}'
                  ' \nor q to quit'
            )

        display_prompt(msg)

        player_input = input().strip()

    if player_input == 'q':
        display_prompt('Goodbye!')
        sys.exit()

    board[int(player_input)] = PLAYER_MARKER


def computer_marks_square(board):
    available_squares = get_available_squares(board)
    winning_lines = get_winning_lines()

    for line in winning_lines:
        square = get_strategic_square(line, board, 'offense')
        if square:
            break

    if not square:
        for line in winning_lines:
            square = get_strategic_square(line, board, 'defense')
            if square:
                break

    if not square:
        for line in winning_lines:
            square = get_strategic_square(line, board, 'potential_win')
            if square:
                break

    if not square and board[OPTIMAL_SQUARE] == AVAILABLE_MARKER:
        square = OPTIMAL_SQUARE

    if not square:
        square = random.choice(available_squares)

    board[square] = COMPUTER_MARKER


def choose_square(board, current_player):
    if current_player == 'player':
        player_marks_square(board)
    else:
        computer_marks_square(board)


def increment_scores(winner, scores):
    if winner == 'computer':
        scores['computer'] += 1
    elif winner == 'player':
        scores['player'] += 1


def play_a_game(current_player, current_scores):
    board = initialize_board()
    #  Keep playing rounds until there's a winner or the board is full
    while True:
        display_board(board, current_scores)

        choose_square(board, current_player)

        winner = get_game_winner(board)
        if winner or board_full(board):
            break

        current_player = get_alternate_player(current_player)

    display_board(board, current_scores)

    return winner if winner else 'tie'

def initialize_match():
    scores = {
        'player' : 0,
        'computer' : 0,
    }

    games_to_match = prompt_games_to_match_number()

    clear_screen()
    display_prompt('Great! '
               f'Whoever wins {games_to_match} games, wins the match!')

    game_start_flag = (prompt_game_start_selection()
                        if GAME_START  == 'choose'
                        else GAME_START)

    match_config = {
        'scores': scores,
        'games_to_match': games_to_match,
        'game_start_flag': game_start_flag,
    }

    return match_config


# Main function
def play_tic_tac_toe():
    display_welcome_message()

    ttt_match = initialize_match()
    scores = ttt_match['scores']
    game_start_flag = ttt_match['game_start_flag']
    games_to_match = ttt_match['games_to_match']

    # Keep playing matches until player decides to stop
    while True:
        game_outcome = play_a_game(game_start_flag, scores)

        if game_outcome in ('computer', 'player'):
            increment_scores(game_outcome, scores)

        if games_to_match in scores.values():
            display_match_winner(game_outcome)

            # Player can decide to play again
            # after the match is over
            if prompt_play_again():
                clear_screen()
                ttt_match = initialize_match()
                scores = ttt_match['scores']
                game_start_flag = ttt_match['game_start_flag']
                games_to_match = ttt_match['games_to_match']
            else:
                display_prompt('Goodbye then!')
                break
        else:
            display_game_outcome(game_outcome)
            display_current_scores(scores)
            # Prompting user to click enter so the outcome stays on-screen
            prompt_to_continue()


play_tic_tac_toe()