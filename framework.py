__author__ = "byteme8bit"

# File imports

# Module imports
from random import randint
from datetime import datetime


class ByteDyce:
    """
    The ByteDyce class contains parameters to store various information for the current and past simulations.
    """

    def __init__(self):
        print("\nWelcome to the ByteDyce Simulation.\n"
              "This program allows you to simulate dice rolls for whatever your needs may be. DnD, Board games, etc.\n")
        self.session_id = datetime.now().strftime("%d-%m-%Y @ %H-%M-%S")
        self.simulations_performed = 0  # Counts number of simulations performed in current session
        self.results = {}  # Stores simulation results. Key = simulation #, Value = results
        self.max_dice = 0  # Stores the highest number of dice simulated in current session
        self.max_sides = 0  # Stores the highest number of dice sides simulation in current session
        self.dice = 0  # Stores the current number of dice
        self.total_sides = 0  # Stores the current number of dice sides
        self.current_sim = []  # Stores the results of current simulation

    # def __del__(self):
    #     self.simulation_to_file()
    #     quit(0)

    def find_max_dice(self, new, current):  # Stores highest number of dice simulated
        self.max_dice = new if new > current else current

    def find_max_sides(self, new, current):  # Stores highest number of sides of dice simulated
        self.max_sides = new if new > current else current

    def store_results(self, results):  # Stores results from each simulation then increases counter by 1
        self.results[self.simulations_performed] = results, self.max_dice, self.max_sides
        self.simulations_performed += 1

    def print_results(self):
        print(f"\nHighest number of dice rolled: {self.max_dice}\n"
              f"Highest number of sides per dice: {self.max_sides}\n")

        for key in self.results.keys():
            print(f"Simulation #{key + 1}:\n"
                  f"Results: {self.results[key][0]}\n"
                  f"Dice rolled: {self.results[key][1]}\n"
                  f"Sides per dice: {self.results[key][2]}")
        print()

    def get_dice_input(self):
        # Total number of dice
        dice = input("\nHow many dice would you like to roll?:\n")

        # Input verification to ensure user provides a number
        while not dice.isnumeric():
            print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
            dice = input("\nHow many dice would you like to roll?:\n")

        self.dice = int(dice)

        self.find_max_dice(self.dice, self.max_dice)

        # Total number of sides for dice
        sides = input("\nHow many sides should each dice have?:\n")

        # Input verification to ensure user provides a number
        while not sides.isnumeric():
            print("\nPlease input a digit (e.g. 1, 3, 574, etc.)")
            sides = input("\nHow many sides should each dice have?:\n")

        self.total_sides = int(sides)

        self.find_max_sides(self.total_sides, self.max_sides)

    def roll_dice(self):
        # Creates list by looping "dice" times and selecting random numbers in range 1 thru "total_sides"
        self.current_sim = [randint(1, int(self.total_sides)) for i in range(int(self.dice))]

        # Splats list to UI and stores simulation results
        print("\n", *self.current_sim, "\n")
        self.store_results(self.current_sim)

    def simulation_to_file(self):
        filename = ".\\" + self.session_id + ".txt"
        file = open(filename, "w")
        file.write(f"ByteDyce Simulation performed {self.session_id}\n"
                   f"Number of simulations performed: {self.simulations_performed}\n"
                   f"Max Dyce Rolled: \t{self.max_dice}\n"
                   f"Max Dyce Sides: \t{self.total_sides}\n\n")

        for key in self.results.keys():
            file.write(f"Simulation #{key + 1}:\n"
                       f"Results: {self.results[key][0]}\n"
                       f"Dice rolled: {self.results[key][1]}\n"
                       f"Sides per dice: {self.results[key][2]}\n\n")
        file.close()



