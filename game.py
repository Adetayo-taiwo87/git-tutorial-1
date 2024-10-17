import random
from random import choices


def play_rps():
    choices = ['rock', 'paper','scissors']
    users_choice = input('your choice:')
    computer = random.choice(choices )
    print(f"computer chose {computer}")


    if users_choice == computer:
        print('tie')
    elif users_choice != computer:
        print('you won')
"""
    elif (users_choice == 'rock' and computer == 'paper') or \
            (users_choice == 'paper' and computer == 'scissors') or \
            (users_choice == 'scissors' and computer == 'rock'):
        print('you win')
    else:
        print('you lose')
"""


play_rps()
