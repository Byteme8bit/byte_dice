__author__ = "byteme8bit"

# File imports

# Module imports
import random

# Total number of dice
dice = input("How many dice would you like to roll?:\n")

# Total number of sides for dice
total_sides = input("How many sides should each dice have?:\n")

# Main loop
while True:

    # Empty list to contain results
    results = []

    # Loops to simulate each dice rolling
    for i in range(int(dice)):

        # Appends a randomly chosen integer to the results list
        results.append(random.randint(1, int(total_sides)))

    # Displays the "dice rolls"
    print(*results)

    # Asks user if program should repeat same parameters or use new ones
    after_results = input("Would you like to repeat this simulation or change the parameters?:\n"
                          "[R]epeat   |   [C]hange   |   [Q]uit")

    # If user chooses to repeat
    if after_results == 'R' or 'r':
        continue

    # If user chooses to quit program
    elif after_results == 'Q' or 'q':
        quit(8)

    # If user chooses to change parameters
    else:
        dice = input("How many dice would you like to roll?:\n")
        total_sides = input("How many sides should each dice have?:\n")
