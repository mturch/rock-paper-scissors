import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()  # Quit the program.
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # Break out of the player's move loop.
        print('Type one of r, p, s, or q.')

    # Display the player's move:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    random_num = random.randint(1, 3)
    if random_num == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_num == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_num == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    elif (player_move == 'r' and computer_move == 'p') or (player_move == 'p' and computer_move == 's') or (player_move == 's' and computer_move == 'r'):
        print('You lose!')
        losses += 1
