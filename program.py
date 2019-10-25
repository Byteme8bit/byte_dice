__author__ = "byteme8bit"

# File imports

# Module imports
from random import randint


class ByteDyce:

    def __init__(self):
        self.simulations_performed = 0
        self.results = {}
        self.max_dice = 0
        self.max_sides = 0
        self.dice = 0
        self.total_sides = 0
        self.current_sim = []

    def find_max_dice(self, new, current):  # Stores highest number of dice simulated
        self.max_dice = new if new > current else current

    def find_max_sides(self, new, current):  # Stores highest number of sides of dice simulated
        self.max_sides = new if new > current else current

    def store_results(self, results):  # Stores results from each simulation
        self.results[self.simulations_performed] = results, self.max_dice, self.max_sides
        self.simulations_performed += 1

    def print_results(self):
        print(f"\nHighest number of dice rolled: {self.max_dice}\n"
              f"Highest number of sides per dice: {self.max_sides}\n")
        for key in self.results.keys():
            print(f"Simulation #{key}:\n"
                  f"Results: {self.results[key][0]}\n"
                  f"Dice rolled: {self.results[key][1]}\n"
                  f"Sides per dice: {self.results[key][2]}")

    def get_dice_input(self):
        # Total number of dice
        d = input("\nHow many dice would you like to roll?:\n")

        # Input verification to ensure user provides a number
        while not d.isnumeric():
            print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
            d = input("\nHow many dice would you like to roll?:\n")

        self.dice = int(d)

        self.find_max_dice(self.dice, self.max_dice)

        # Total number of sides for dice
        t = input("\nHow many sides should each dice have?:\n")

        # Input verification to ensure user provides a number
        while not t.isnumeric():
            print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
            t = input("\nHow many sides should each dice have?:\n")

        self.total_sides = int(t)

        self.find_max_sides(self.total_sides, self.max_sides)

    def roll_dice(self):

        # self.dice, self.total_sides = self.get_dice_input()

        # Main loop
        while True:

            # Creates list by looping "dice" times and selecting random numbers in range 1 thru "total_sides"
            self.current_sim = [randint(1, int(self.total_sides)) for i in range(int(self.dice))]

            # Splats list
            print("\n", *self.current_sim, "\n")
            self.store_results(self.current_sim)

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
                self.get_dice_input()

            # If user chooses to repeat
            elif after_results == 'r':
                pass

            elif after_results == 'p':
                self.print_results()

            # If user chooses to quit program
            else:
                quit(8)


program = ByteDyce()

print("\nWelcome to the ByteDyce Simulation.\n"
      "This program allows you to simulate dice rolls for whatever your needs may be. DnD, Board games, etc.\n")

program.get_dice_input()
program.roll_dice()
