#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors

# Imports
from calculators import algebra, conversions, stocks, financial, calculator, randomization, bmi, geometry
import restart
import colors
import contribution
import end
import time
from gui import *


def wrong_option():
    print(colors.red + 'User input error found... Restarting user input choice...', colors.reset)
    time.sleep(2)
    start()


INPUT_CHOICES = {
    1: calculator.start,
    2: algebra.start,
    3: geometry.start,
    4: conversions.start,
    5: stocks.start,
    6: financial.start,
    7: randomization.start,
    8: bmi.start,
    9: contribution.start,
    10: restart.restart,
    11: end.end
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
(1) Basic Arithmetic Math        |      (6) Financial Calculator      |      (11) Exit
(2) Algebra Calculator           |      (7) Randomization
(3) Geometry Calculator          |      (8) BMI Calculator
(4) All Converters               |      (9) Credits
(5) Stock Market Calculator      |      (10) Restart              

Which option would you like to use: '''))
    print()

    if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        wrong_option()

    else:
        # get function from dict and execute
        # if option not found then execute wrong option function
        INPUT_CHOICES.get(choice, 11)()


if __name__ == '__main__':
    start()
