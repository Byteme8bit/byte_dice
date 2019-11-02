__author__ = 'byteme8bit'

# File imports
from framework import ByteDyce

# Module imports
import tkinter
from random import randint


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
