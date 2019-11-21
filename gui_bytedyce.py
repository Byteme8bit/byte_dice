__author__ = 'byteme8bit'

# File imports

# Module imports
import tkinter
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

    def find_max_dice(self, new, current):  # Stores highest number of dice simulated
        self.max_dice = new if new > current else current

    def find_max_sides(self, new, current):  # Stores highest number of sides of dice simulated
        self.max_sides = new if new > current else current

    def store_results(self, results):  # Stores results from each simulation then increases counter by 1
        self.results[self.simulations_performed] = results, self.max_dice, self.max_sides
        self.simulations_performed += 1

    def simulation_to_file(self):
        filename = ".\\logs\\" + self.session_id + ".txt"
        file = open(filename, "w")
        file.write(f"ByteDyce Simulation performed {self.session_id}\n"
                   f"Total simulations: \t{self.simulations_performed}\n"
                   f"Max Dyce Rolled: \t{self.max_dice}\n"
                   f"Max Dyce Sides: \t{self.total_sides}\n\n")

        for key in self.results.keys():
            file.write(f"[Simulation #{key + 1}]\n"
                       f"Results: {self.results[key][0]}\n"
                       f"Dice rolled: {self.results[key][1]}\n"
                       f"Sides per dice: {self.results[key][2]}\n\n")
        file.close()

    def optimize_logs(self):
        # Check how many items in \logs\
        # If logs > 100 move to archive folder (and compress?)
        # Else skip
        pass


# Status of program
status = 'Beta'


def run_simulation():
    program.dice = int(d_input.get())
    program.find_max_dice(program.dice, program.max_dice)
    program.total_sides = int(t_input.get())
    program.find_max_sides(program.total_sides, program.max_sides)
    program.current_sim = [randint(1, int(program.total_sides)) for i in range(program.dice)]
    results.insert(1, program.current_sim)
    program.store_results(program.current_sim)


def clear_results():
    results.delete(0, 'end')
    results.insert(0, 'Results: ')


# ============================================= GUI START =============================================
# MAIN WINDOW
mainWindow = tkinter.Tk()
mainWindow.title(f'Byte Dyce - - {status}')
mainWindow.geometry('400x250')
mainWindow.minsize(400, 250)

# Header
header = tkinter.Label(mainWindow, text='Byte Dyce: Dice Roll Simulator')
header.grid(row=1, column=1, sticky='nsew')

# Options Frame
optionsFrame = tkinter.LabelFrame(mainWindow, text='Options')
optionsFrame.grid(row=2, column=1, sticky='')

# Dice Label
d_label = tkinter.Label(optionsFrame, text='# Dice to roll: ')
d_label.grid(row=1, column=1, sticky='e')

# Dice Input
d_input = tkinter.Entry(optionsFrame)
d_input.grid(row=1, column=2, sticky='w')
d_input.insert(0, '1')

# Sides Label
t_label = tkinter.Label(optionsFrame, text='# of Sides per Dice: ')
t_label.grid(row=2, column=1, sticky='e')

# Sides Input
t_input = tkinter.Entry(optionsFrame)
t_input.grid(row=2, column=2, sticky='w')
t_input.insert(0, '6')

# Roll the Dice Button
rtd_label = tkinter.Button(optionsFrame, text='Roll the Dice', command=run_simulation)
rtd_label.grid(row=1, rowspan=2, column=3, sticky='nse')

# Results Box
results = tkinter.Listbox(mainWindow)
results.grid(row=3, column=1, sticky='nsew')
results.insert(0, 'Results: ')

# Clear Button
clrButton = tkinter.Button(optionsFrame, text='Clear Results', command=clear_results)
clrButton.grid(row=1, rowspan=2, column=4, sticky='nsew')

# Weights - Rows
mainWindow.rowconfigure(0, weight=10)       # Border
mainWindow.rowconfigure(1, weight=100)      # Header
mainWindow.rowconfigure(2, weight=100)      # Options #1
mainWindow.rowconfigure(3, weight=100)      # Options #2
mainWindow.rowconfigure(4, weight=100)      # Results Box
mainWindow.rowconfigure(5, weight=10)       # Border

# Weights - Columns
mainWindow.columnconfigure(0, weight=10)    # Border
mainWindow.columnconfigure(1, weight=100)   # Content
mainWindow.columnconfigure(2, weight=10)    # Border

# ========================================== GUI END =======================================

program = ByteDyce()

mainWindow.mainloop()

program.simulation_to_file()
