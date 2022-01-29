#FLOW CONTROL
# Using break and control can let you move on or re-start loops mid-loop.

import random, sys

print('ROCK,PAPER,SCISSORS')

#these variable keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

# Main Game Loop
while True: 
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    # The player input loop
    while True: 
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r,p,s, or q.')

    # Display the Player Choice
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display the Computer Choice
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record win/loss/tie
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties +1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins+1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins+1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins+1
    elif computerMove == 'r' and playerMove == 's':
        print('You Lose!')
        losses = losses + 1
    elif computerMove == 'p' and playerMove == 'r':
        print('You Lose!')
        losses = losses + 1
    elif computerMove == 's' and playerMove == 'p':
        print('You Lose!')
        losses = losses + 1
    