#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors


# Imports
import calculators.calculators
import conversions.conversions
import time
from modules import restart, contribution, end, colors
from gui import *


def wrong_option():
    print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
    time.sleep(2)
    start()


INPUT_CHOICES = {
    1: calculators.calculators.start,
    2: conversions.conversions.start,
    3: contribution.start,
    4: restart.restart,
    5: end.end
}


def start():
    choice = str(
        input('Want to run the GUI version of this project (yes / no): '))
    print()

    if choice.lower() in ['y', 'yes', 'sure', 'yep']:
        print(colors.green, 'GUI Application is now running!\n', colors.reset)
        start_gui()
    elif choice.lower() in ['n', 'no', 'nope', 'nah']:
        pass
    else:
        wrong_option()

    print(colors.green + 'All Calculators and Converters', colors.reset)
    choice = int(input('''
(1) All Calculators            
(2) All Converters
(3) Credits
(4) Restart  
(5) Exit             

Which option would you like to use: '''))
    print()

    if choice not in [1, 2, 3, 4, 5]:
        wrong_option()

    else:
        # get function from dict and execute
        # if option not found then execute wrong option function
        INPUT_CHOICES.get(choice, 5)()


if __name__ == '__main__':
    start()
