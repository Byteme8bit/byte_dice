__author__ = "byteme8bit"

# File imports
from framework import ByteDyce

# Module imports

program = ByteDyce()

program.get_dice_input()

# Main loop
while True:

    program.roll_dice()

    # Asks user if program should repeat same parameters or use new ones
    after_results = input("\nWould you like to repeat this simulation or change the parameters?:\n"
                          "[R]epeat   |   [C]hange    |   [P]rint Results   |   [Q]uit\n").lower()

    # Input verification to ensure user provides a valid response
    while after_results not in "rcpq" or len(after_results) > 1:
        print("\nPlease select valid answer r - c - p - q")
        after_results = input("\nWould you like to repeat this simulation or change the parameters?:\n"
                              "[R]epeat   |   [C]hange   |   [P]rint Results   |   [Q]uit\n").lower()

    # If user chooses to change parameters
    if after_results == 'c':
        program.get_dice_input()

    # If user chooses to repeat
    elif after_results == 'r':
        pass

    # If user chooses to print stored results of past simulations
    elif after_results == 'p':
        program.print_results()

    # If user chooses to quit program
    else:
        program.simulation_to_file()
        quit(8)
