#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors


# Imports
import calculators.calculators
import conversions.conversions
import time
from modules import restart, contribution, end, colors, release
from modules.currency_api import create_key_json
from modules.errors import Restart, Exit
from gui import *


def error_message():
    """
A basic error message for when something doesn't work correctly or logical statements fail.
    """
    print(colors.red + "Invalid Choice...\n", colors.reset)
    time.sleep(2)
    start()


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
(4) Releases
(5) Credits
(6) Exit

Which option would you like to use: '''))
        print()

        if choice == 1:
            try:
                calculators.calculators.start()
            except Exit:
                break
        elif choice == 2:
            conversions.conversions.start()
        elif choice == 3:
            print(colors.green + 'GUI Application is now running!\n', colors.reset)
            start_gui()
        elif choice == 4:
            release.start()
        elif choice == 5:
            contribution.start()
        elif choice == 6:
            break
        else:
            error_message()
    print('Exiting...')


if __name__ == '__main__':
    create_key_json()
    start()
