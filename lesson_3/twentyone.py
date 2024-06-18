""" 
INITIALIZE DECK 

{
    'suit' : hearts/spades/etc.,
    'face': king, 2, etc.,
    'value': 2, 10, etc.
    'state': dealt / available 
}

## Algorithm   
1. List possible suits
2. List possible values. 
3. Iterate over suits. For each suit.
    Iterate over values. For each value:
        - Create a "card" object depending on the value of the face, in 'available' state
        - Add the card to the list of cards
    Add ace card 


"""
import random 
import sys

SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
NUMBER_CARDS= range(2, 11)
NAME_CARDS = ['jack', 'queen', 'king', 'ace']
INITIAL_HAND_SIZE = 2
DEALER_HAND_TARGER = 17


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
            card ={
                'suit': suit,
                'face': name,
                'value': 10 if name != 'ace' else 0,
                'available': True
            }
            deck.append(card)

    return deck 


def deal_initial_hand(deck):
    return [get_random_card(deck) for _ in range(INITIAL_HAND_SIZE)]


def get_random_card(deck):
    available_cards = [ index for index, card in enumerate(deck) if card['available'] ]
    
    if not available_cards:
        return {}
    
    card_number = random.choice(available_cards)
    
    deck[card_number]['available'] = False
    
    return deck[card_number]


def calculate_hand_value(hand):
    hand_value = 0

    non_ace_cards = [ card['value'] for card in hand if card['face'] != 'ace' ]
    hand_value += sum(non_ace_cards)

    ace_cards = [ card['value'] for card in hand if card['face'] == 'ace' ]
    for ace in ace_cards:
        if hand_value + 11 <= 21:
            hand_value += 11
        else:
            hand_value += 1

    return hand_value

def compare_cards(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value > dealer_value:
        return 'player'
    elif player_value < dealer_value:
        return 'dealer'
    else:
        return 'tie'


def display_prompt(message):
    print(f'==> {message}')


def display_player_hand(hand):
    cards_overview = [f"{card['face'].capitalize()} "
                      f"of {card['suit'].capitalize()}"
                      for card in hand]
    hand_value = calculate_hand_value(hand)

    display_prompt(f'You have: {', '.join(cards_overview)} (Score: {hand_value})')


def display_dealer_hand(hand, uncovered = False):
    # TESTING ---- 
    uncovered = True

    if not uncovered:
        card_1 = (f"{hand[0]['face'].capitalize()} of "
        f"{hand[0]['suit'].capitalize()}")

        display_prompt(f"Dealer has: {card_1} and ***** ")
    else:
        cards_overview = [f"{card['face'].capitalize()} "
                      f"of {card['suit'].capitalize()}"
                      for card in hand]
        hand_value = calculate_hand_value(hand)

        display_prompt(f'Dealer Has: {', '.join(cards_overview)} (Score: {hand_value})')


def display_winner(game_outcome):
    match game_outcome:
        case 'player':
            display_prompt('Congratulations, you won the game!')
        case 'dealer':
            display_prompt('Sorry, dealer has won!') 
        case 'tie': 
            display_prompt("It's a tie!")


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


def player_takes_turn(player_hand, deck):
    while True:
        player_decision = prompt_player_decision()
        if player_decision == 'stay':
            return 'stay'
        else:
            # TODO ask for advice in code review if this is fine
            player_hand.append(get_random_card(deck))
            display_player_hand(player_hand)
            if calculate_hand_value(player_hand) > 21:
                return 'bust'
            

def dealer_takes_turn(dealer_hand, deck):
    while calculate_hand_value(dealer_hand) < 17:
        # TODO ask for advice in code review
        dealer_hand.append(get_random_card(deck))
        if calculate_hand_value(dealer_hand) > 21:
            return 'bust'
    
    return 'stay'
    

def play_21():
    

    """ 
    1. Ask player if he wants to hit or stay. 
    2. If stay, go to "Computer's turn"
    3. If hit:
        A. Add a card to player's hand
        B. Display new hand 
        C. If hand value > 21:
            - Display "player bust" result
            - Go to "Play again?" prompt
        D. Else:
            - Go to step 1.

    """

    while True:
        deck = initialize_deck()

        player_hand = deal_initial_hand(deck)
        dealer_hand = deal_initial_hand(deck)

        display_dealer_hand(dealer_hand)
        print()
        display_player_hand(player_hand)

        # Player's turn 
        player_outcome = player_takes_turn(player_hand, deck)
        if player_outcome == 'bust':        
            display_prompt('Sorry! Your hand is a bust!')
        # If player's hand is not a bust, dealer takes its turn
        else:
            # TODO - dealer's trun function
            dealer_outcome = dealer_takes_turn(dealer_hand, deck)
            display_dealer_hand(dealer_hand, uncovered=True)
            if dealer_outcome == 'bust':
                game_outcome = 'player'
                display_prompt("Dealer's hand is a bust!")
            else:
                # TODO - function to compare the hands and return the winner
                game_outcome = compare_cards(player_hand, dealer_hand)
            
            # TODO - display full dealer's hand - maybe option in curent function
            display_winner(game_outcome)
        
        # TODO - get user's choice to play again or not 
        if not prompt_play_again():
            display_prompt('Goodbye then!')
            break 


play_21()

