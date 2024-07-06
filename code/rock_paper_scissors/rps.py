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
    print("Please enter (r)ock, (p)aper, (s)cissors (any other key to quit)")
    user_input = input()
    # TODO: Can I made the input function require a literal (r/p/s)?
    if user_input not in ['r', 'p', 's']:
        sys.exit()
    if user_input == 'r' or user_input == 'p' or user_input == 's':
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
        return 'r'
    elif computer_input == 2:
        return 'p'
    elif computer_input == 3:
        return 's'


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
    # Ties
    if user_input == computer_input:
        print('It is a tie!')
        TIES += 1
    # User wins
    elif (
        (user_input == 'r' and computer_input == 's') or
        (user_input == 'p' and computer_input == 'r') or
        (user_input == 's' and randomly_generate_computer_input == 'r')
    ):
        print('You win!')
        WINS += 1
    # User loses
    elif(
        (user_input == 's' and computer_input == 'r') or
        (user_input == 'r' and computer_input == 'p') or
        (user_input == 'r' and computer_input == 's')
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
    if user_input == 'r':
        print('ROCK versus...')
    elif user_input == 'p':
        print('PAPER versus...')
    elif user_input == 's':
        print('SCISSORS versus...')
    else:
        print('Invalid input')

    computer_input = randomly_generate_computer_input()

    # Print to stdout
    if computer_input == 'r':
        print('ROCK')
    elif computer_input == 'p':
        print('PAPER')
    elif computer_input == 's':
        print('SCISSORS')

    # Compare all possible outcomes
    play_game()

    # Print the score
    WINS = scoreboard()['Wins']
    LOSSES = scoreboard()['Losses']
    TIES = scoreboard()['Ties']

    # Print the score
    print(f"Wins: {WINS}, Losses: {LOSSES}, Ties: {TIES}")
