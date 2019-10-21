__author__ = "byteme8bit"

# File imports

# Module imports
import random

dice = input("How many dice would you like to roll?:\n")
total_sides = input("How many sides should each dice have?:\n")
game_continue = True

while game_continue:

    results = []

    for i in range(int(dice)):
        results.append(random.randint(1, int(total_sides)))

    print(*results)

    after_results = input("Would you like to repeat this simulation or change the parameters?:\n"
                          "[R]epeat   |   [C]hange")

    if after_results == 'R' or 'r':
        continue

    else:
        dice = input("How many dice would you like to roll?:\n")
        total_sides = input("How many sides should each dice have?:\n")
        game_continue = True





