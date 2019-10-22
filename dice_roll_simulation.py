__author__ = "byteme8bit"

# File imports

# Module imports
import random

# Total number of dice
dice = input("\nHow many dice would you like to roll?:\n")

# Input verification to ensure user provides a number
while not dice.isnumeric():
    print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
    dice = input("\nHow many dice would you like to roll?:\n")

# Total number of sides for dice
total_sides = input("\nHow many sides should each dice have?:\n")

# Input verification to ensure user provides a number
while not total_sides.isnumeric():
    print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
    total_sides = input("\nHow many sides should each dice have?:\n")

# Main loop
while True:

    print()
    # Empty list to contain results
    results = []

    # Loops to simulate each dice rolling
    for i in range(int(dice)):

        # Appends a randomly chosen integer to the results list
        results.append(random.randint(1, int(total_sides)))

    # Displays the "dice rolls"
    print(*results)

    # Asks user if program should repeat same parameters or use new ones
    after_results = input("\nWould you like to repeat this simulation or change the parameters?:\n"
                          "[R]epeat   |   [C]hange   |   [Q]uit\n").lower()

    # Input verification to ensure user provides a valid response
    while after_results not in "rcq" or len(after_results) > 1:
        print("\nPlease select valid answer r - c - q")
        after_results = input("\nWould you like to repeat this simulation or change the parameters?:\n"
                              "[R]epeat   |   [C]hange   |   [Q]uit\n").lower()

    # If user chooses to change parameters
    if after_results == 'c':

        # Total number of dice
        dice = input("How many dice would you like to roll?:\n")

        while not dice.isnumeric():
            print("Please input a numeric\n")
            dice = input("How many dice would you like to roll?:\n")

        # Total number of sides for dice
        total_sides = input("How many sides should each dice have?:\n")

        while not total_sides.isnumeric():
            print("Please input a numeric\n")
            total_sides = input("How many sides should each dice have?:\n")

    # If user chooses to repeat
    elif after_results == 'r':
        continue

    # If user chooses to quit program
    else:
        quit(8)
