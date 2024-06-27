import random
import os

SUITS = ('hearts', 'diamonds', 'clubs', 'spades')
NUMBER_CARDS= range(2, 11)
NAME_CARDS = ('jack', 'queen', 'king', 'ace')
INITIAL_HAND_SIZE = 2
DEALER_HAND_TARGET = 17
ROUNDS_TO_WIN = 3
SCORE_TARGET = 21


def display_prompt(message):
    print(f'==> {message}')


def display_welcome_message():
    display_prompt(f'Welcome to {SCORE_TARGET}!')
    display_prompt(f'Win {ROUNDS_TO_WIN} rounds to win the game!\n')


def display_scores(scores):
    dealer = scores['dealer']
    player = scores['player']

    display_prompt(f'Current Score: Player {player} | Dealer {dealer}')


def display_player_hand(hand):
    cards = hand['cards']
    cards_overview = [f"{card['face'].capitalize()} "
                      f"of {card['suit'].capitalize()}"
                      for card in cards]

    display_prompt(f'You have: {', '.join(cards_overview)} '
                   f'(Score: {hand['value']})')


def display_dealer_hand(hand, uncovered = False):
    cards = hand['cards']

    if not uncovered:
        card_1 = (f"{cards[0]['face'].capitalize()} of "
        f"{cards[0]['suit'].capitalize()}")

        display_prompt(f"Dealer has: {card_1} and ***** ")
    else:
        cards_overview = [f"{card['face'].capitalize()} "
                      f"of {card['suit'].capitalize()}"
                      for card in cards]

        display_prompt(f'Dealer Has: {', '.join(cards_overview)} '
                       f'(Score: {hand['value']})')


def display_round_result(round_outcome):
    match round_outcome:
        case 'player':
            display_prompt('Congratulations, you win the round.\n')
        case 'dealer':
            display_prompt('Sorry! dealer wins the round.\n')
        case 'tie':
            display_prompt("It's a tie!\n")


def display_game_winner(round_outcome):
    if round_outcome == 'player':
        msg = 'Congratulations you win the game.'
    else:
        msg = 'Sorry! dealer wins the game.'

    display_prompt(msg)


def prompt_player_decision():
    display_prompt('Enter "h" to Hit or "s" to Stay:')
    player_input = input().strip().lower()

    while player_input not in ('hit', 'h', 'stay', 's'):
        display_prompt('Invalid entry. Enter "h" to Hit or "s" to Stay')
        player_input = input()

    return 'hit' if player_input in ('hit', 'h') else 'stay'


def prompt_play_again():
    display_prompt('Play again? Enter y/n')
    player_input = input().strip().lower()
    while player_input not in ('y', 'n', 'yes', 'no'):
        display_prompt('Invalid input. Enter y/n')
        player_input = input()

    return player_input in ('y', 'yes')

def initialize_scores():
    return {
        'player' : 0,
        'dealer' : 0,
    }

def initialize_deck():
    deck = []

    for suit in SUITS:
        for number in NUMBER_CARDS:
            card = {
                'suit': suit,
                'face': str(number),
                'value': number,
                'available': True
            }
            deck.append(card)

        for name in NAME_CARDS:
            card = {
                'suit': suit,
                'face': name,
                'value': 10 if name != 'ace' else 11,
                'available': True
            }
            deck.append(card)

    return deck


def deal_initial_hand(deck):
    cards = [ get_random_card(deck) for _ in range(INITIAL_HAND_SIZE) ]
    value = calculate_hand_value(cards)

    return {
        'cards': cards,
        'value': value,
    }


def get_random_card(deck):
    available_cards = [ card for card in deck if card['available'] ]

    if not available_cards:
        return {}

    dealt_card = random.choice(available_cards)

    dealt_card['available'] = False

    return dealt_card


def calculate_hand_value(cards):
    hand_value = 0

    non_ace_cards = [ card['value'] for card in cards
                     if card['face'] != 'ace' ]
    hand_value += sum(non_ace_cards)

    ace_cards = [ card['value'] for card in cards
                 if card['face'] == 'ace' ]
    for ace in ace_cards:
        if hand_value + 11 <= SCORE_TARGET:
            hand_value += 11
        else:
            hand_value += 1

    return hand_value


def calculate_round_winner(player_hand, dealer_hand):

    if player_hand['value'] > dealer_hand['value']:
        return 'player'
    elif player_hand['value'] < dealer_hand['value']:
        return 'dealer'
    else:
        return 'tie'


def update_scores(round_outcome, scores):
    if round_outcome == 'dealer':
        scores['dealer'] += 1
    elif round_outcome == 'player':
        scores['player'] += 1

    return scores


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def player_takes_turn(player_hand, deck):
    cards = player_hand['cards']

    while True:
        player_decision = prompt_player_decision()
        if player_decision == 'stay':
            return 'stay'
        else:
            cards.append(get_random_card(deck))

            player_hand['value'] = calculate_hand_value(cards)

            display_player_hand(player_hand)

            if player_hand['value'] > SCORE_TARGET:
                return 'bust'


def dealer_takes_turn(dealer_hand, deck):
    cards = dealer_hand['cards']

    while dealer_hand['value'] < DEALER_HAND_TARGET:
        cards.append(get_random_card(deck))
        dealer_hand['value'] = calculate_hand_value(cards)

        if dealer_hand['value'] > SCORE_TARGET:
            return 'bust'

    return 'stay'


def play_round():
    display_prompt('Press Enter to start the next round')
    input()
    clear_screen()

    deck = initialize_deck()

    player_hand = deal_initial_hand(deck)
    dealer_hand = deal_initial_hand(deck)

    display_dealer_hand(dealer_hand)
    print()
    display_player_hand(player_hand)

    player_outcome = player_takes_turn(player_hand, deck)
    if player_outcome == 'bust':
        display_prompt('Sorry! Your hand is a bust!')
        round_outcome = 'dealer'
    else:
        dealer_outcome = dealer_takes_turn(dealer_hand, deck)
        display_dealer_hand(dealer_hand, uncovered = True)
        if dealer_outcome == 'bust':
            display_prompt("Dealer's hand is a bust!")
            round_outcome = 'player'
        else:
            round_outcome = calculate_round_winner(player_hand, dealer_hand)

    return round_outcome


def play_21():
    while True:
        clear_screen()
        display_welcome_message()

        scores = initialize_scores()

        while (scores['player'] < ROUNDS_TO_WIN
               and scores['dealer'] < ROUNDS_TO_WIN):
            round_outcome = play_round()

            display_round_result(round_outcome)

            scores = update_scores(round_outcome, scores)

            display_scores(scores)

        print('')
        # Whoever won the last round is the winner of the game
        display_game_winner(round_outcome)

        if not prompt_play_again():
            display_prompt('Goodbye then!')
            break



play_21()