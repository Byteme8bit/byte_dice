__author__ = "byteme8bit"

# File imports

# Module imports
from random import randint


def get_dice_input():
    # Total number of dice
    d = input("\nHow many dice would you like to roll?:\n")
    
    # Input verification to ensure user provides a number
    while not d.isnumeric():
        print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
        d = input("\nHow many dice would you like to roll?:\n")
    
    # Total number of sides for dice
    t = input("\nHow many sides should each dice have?:\n")
    
    # Input verification to ensure user provides a number
    while not t.isnumeric():
        print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
        t = input("\nHow many sides should each dice have?:\n")
    
    return d, t


def roll_dice(d=None, t=None, r=None):

    # Checks for override, grabs user input if no overrides
    dice = d if not d else d
    total_sides = t if not t else t

    if not d and not t:
        dice, total_sides = get_dice_input()

    # Main loop
    while True:

        # Splats list created by looping "dice" times and selecting random numbers in range 1 - "total_sides"
        print("\n", *[randint(1, int(total_sides)) for i in range(int(dice))], "\n")

        # Asks user if program should repeat same parameters or use new ones
        after_results = input("\nWould you like to repeat this simulation or change the parameters?:\n"
                              "[R]epeat   |   [C]hange   |   [Q]uit\n").lower() if not r else r

        # Input verification to ensure user provides a valid response
        while after_results not in "rcq" or len(after_results) > 1:
            print("\nPlease select valid answer r - c - q")
            after_results = input("\nWould you like to repeat this simulation or change the parameters?:\n"
                                  "[R]epeat   |   [C]hange   |   [Q]uit\n").lower()

        # If user chooses to change parameters
        if after_results == 'c':
            dice, total_side = get_dice_input()

        # If user chooses to repeat
        elif after_results == 'r':
            continue

        # If user chooses to quit program
        else:
            quit(8)


roll_dice()
