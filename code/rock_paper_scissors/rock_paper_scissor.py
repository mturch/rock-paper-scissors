import random, sys

# Declare global variables
# User input function
# convert user input to int
# computer input function
# Convert user input to int
# Compare user input to computer input
# Display the result
# Increment the score

# Define function to request user input
def get_user_input() -> str:
    """
    Request user input

    Args:
        None
    Returns:
        str: user input
    """
    print("Please enter (R)ock, (P)aper, (S)cissors (any other key to quit)")
    user_input = input()
    user_input = user_input.upper()
    # TODO: Can I made the input function require a literal (r/p/s)?
    if user_input not in ['R', 'P', 'S']:
        sys.exit()
    if user_input == 'R' or user_input == 'P' or user_input == 'S':
        return user_input


# Define function to randomly generate computer input
def randomly_generate_computer_input() -> str:
    """
    Generate the computer input
    Args:
        None
    Returns:
        str: computer input
    """
    computer_input = random.randint(1, 3)
    if computer_input == 1:
        return 'R'
    elif computer_input == 2:
        return 'P'
    elif computer_input == 3:
        return 'S'


def play_game() -> str:
    """
    Function to compare user input to computer input
    Args:
        None
    Returns:
        str: result of the game
        (win, lose, tie update the global)
    """
    global user_input
    global computer_input
    global WINS
    global LOSSES
    global TIES

    user_input = user_input.upper()

    # Ties
    if user_input == computer_input:
        print('It is a tie!')
        TIES += 1

    # User wins
    elif (
        (user_input == 'R' and computer_input == 'S') or
        (user_input == 'P' and computer_input == 'R') or
        (user_input == 'S' and computer_input == 'R')
    ):
        print('You win!')
        WINS += 1

    # User loses
    elif(
        (user_input == 'S' and computer_input == 'R') or
        (user_input == 'R' and computer_input == 'P') or
        (user_input == 'R' and computer_input == 'S')
    ):
        print('You lose!')
        LOSSES += 1


def scoreboard() -> dict:
    global WINS
    global LOSSES
    global TIES

    series_score = {
        'Wins': WINS,
        'Losses': LOSSES,
        'Ties': TIES
    }
    return series_score

# Global variables
WINS : int = 0
LOSSES : int = 0
TIES : int = 0

while True:
    while True:
        user_input = get_user_input()
        break
        print('Enter r, p, or s.')

    # Print to stdout
    if user_input == 'R':
        print('ROCK versus...')
    elif user_input == 'P':
        print('PAPER versus...')
    elif user_input == 'S':
        print('SCISSORS versus...')
    else:
        print('Invalid input; Exiting game.')
        sys.exit()

    computer_input = randomly_generate_computer_input()

    # Print to stdout
    if computer_input == 'R':
        print('ROCK')
    elif computer_input == 'P':
        print('PAPER')
    elif computer_input == 'S':
        print('SCISSORS')

    # Compare all possible outcomes
    play_game()

    # Print the score
    WINS = scoreboard()['Wins']
    LOSSES = scoreboard()['Losses']
    TIES = scoreboard()['Ties']

    # Print the score
    print(f"Wins: {WINS}, Losses: {LOSSES}, Ties: {TIES}")
