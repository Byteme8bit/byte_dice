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
    program.total_sides = int(t_input.get())
    results.insert(1, [randint(1, int(program.total_sides)) for i in range(program.dice)])


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
optionsFrame.grid(row=2, column=1, sticky='nsew')

# Dice Label
d_label = tkinter.Label(optionsFrame, text='# Dice to roll: ')
d_label.grid(row=1, column=1, sticky='w')

# Dice Input
d_input = tkinter.Entry(optionsFrame)
d_input.grid(row=1, column=2, sticky='e')

# Sides Label
t_label = tkinter.Label(optionsFrame, text='# of Sides per Dice: ')
t_label.grid(row=2, column=1, sticky='w')

# Sides Input
t_input = tkinter.Entry(optionsFrame)
t_input.grid(row=2, column=2, sticky='e')

# Roll the Dice Button
rtd_label = tkinter.Button(optionsFrame, text='Roll the Dice', command=run_simulation)
rtd_label.grid(row=1, rowspan=2, column=3, sticky='nsew')

# Results Box
results = tkinter.Listbox(mainWindow)
results.grid(row=3, rowspan=2, column=1, sticky='ew')


# Weights - Rows
mainWindow.rowconfigure(0, weight=10)
mainWindow.rowconfigure(1, weight=100)
mainWindow.rowconfigure(2, weight=100)
mainWindow.rowconfigure(3, weight=50)
mainWindow.rowconfigure(4, weight=10)

# Weights - Columns
mainWindow.columnconfigure(0, weight=10)
mainWindow.columnconfigure(1, weight=100)
mainWindow.columnconfigure(2, weight=10)

# ========================================== GUI END =======================================

program = ByteDyce()


mainWindow.mainloop()
