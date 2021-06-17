#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors


# Imports
import calculators.calculators
import conversions.conversions
import time
from modules import restart, contribution, end, colors, release
from gui import *


def error_message():
    print(colors.red + "Invalid Choice...\n", colors.reset)
    time.sleep(2)
    start()


def start():
    print(colors.green + 'All Calculators and Converters', colors.reset)
    choice = int(input('''
(1) All Calculators            
(2) All Converters
(3) GUI Version
(4) Releases
(5) Credits
(6) Restart  
(7) Exit             

Which option would you like to use: '''))
    print()

    if choice == 1:
        calculators.calculators.start()
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
        restart.restart()
    elif choice == 7:
        end.end()
    else:
        error_message()


if __name__ == '__main__':
    start()
