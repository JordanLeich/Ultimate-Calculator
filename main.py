#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors


# Imports
import calculators.calculators
import conversions.conversions
from modules import extras, colors
from modules.errors import Exit
from gui import *


def start():
    """
This is the first user input choice an end-user would receive, this is a main ui hub to access all the other areas of
this project.
    """
    while True:
        print(colors.green + 'All Calculators and Converters', colors.reset)
        choice = int(input('''
(1) All Calculators
(2) All Converters
(3) GUI Version
(4) Extras
(5) Exit

Which option would you like to use: '''))
        print()

        if choice == 1:
            try:
                calculators.calculators.start()
            except Exit:
                break
        elif choice == 2:
            try:
                conversions.conversions.start()
            except Exit:
                break
        elif choice == 3:
            print(colors.green + 'GUI Application is now running!\n', colors.reset)
            start_gui()
        elif choice == 4:
            extras.start()
        elif choice == 5:
            break
        else:
            print(colors.red + "Invalid Choice...\n", colors.reset)
    print("Reached end of the program... Ending program...\n")


if __name__ == '__main__':
    start()
