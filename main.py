#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors

# Imports
from calculators import algebra, conversions, stocks, financial, calculator, randomization, bmi
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
    3: conversions.start,
    4: stocks.start,
    5: financial.start,
    6: randomization.start,
    7: bmi.start,
    8: contribution.start,
    9: restart.restart,
    10: end.end
}


def start():
    choice = str(
        input('Want to run the GUI version of this project (yes / no): '))
    print()

    if choice.lower() in ['y', 'yes']:
        print(colors.green, 'GUI Application is now running!\n', colors.reset)
        start_gui()
    elif choice.lower() in ['n', 'no']:
        pass
    else:
        print(colors.red + 'User input error found... Restarting input choice...\n', colors.reset)
        time.sleep(2)
        start()

    print(colors.green + 'All Calculators and Converters', colors.reset)
    choice = int(input('''
(1) Basic Arithmetic Math                           |      (6) Randomization (Random Number Generator, Heads or Tails)
(2) Algebra (Find Slope, Pythagorean Theorem)       |      (7) BMI Calculator (Body Mass Index)
(3) All Converters (Temperature, Mass, & More)      |      (8) All Project Contributors
(4) Stock Market Shares Calculator (Gain/Loss)      |      (9) Restart Program
(5) Financial Calculator (Payroll, Tipping)         |      (10) Exit Program

Which option would you like to use: '''))
    print()

    if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        wrong_option()

    else:
        # get function from dict and execute
        # if option not found then execute wrong option function
        INPUT_CHOICES.get(choice, 10)()


if __name__ == '__main__':
    start()
