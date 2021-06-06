#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors

# Imports
from calculators import algebra, time_converter, conversions, stocks, financial, calculator
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
    5: time_converter.start,
    6: financial.start,
    7: contribution.start,
    8: restart.restart,
    9: end.end
}


def start():
    choice1 = str(
        input('Want to run the GUI version of this project (yes / no): '))
    print()

    if choice1.lower() in ['y', 'yes']:
        print(colors.green, 'GUI Application is now running!\n', colors.reset)
        start_gui()
    elif choice1.lower() in ['n', 'no']:
        print('Proceeding to normal calculator...\n')
    else:
        print(colors.red + 'User input error found... Restarting input choice...\n')
        time.sleep(2)
        start()

    print(colors.green + 'All Calculators and Converters!', colors.reset)
    choice2 = int(input('''(1) Basic Arithmetic Math (Add, Subtract, Multiply, Divide, & More)
(2) Algebra (Find Slope, Pythagorean Theorem)
(3) All Converters (Temperature, Mass, Length, Volume)
(4) Stock Market Shares Calculator (Gain/Loss of a stock)
(5) Time Converter (Hours to Days, Days in Years, * More)
(6) Financial Calculator (Payroll, Restaurant Tipping)
(7) All Project Contributors
(8) Restart Program
(9) Exit Program
Which option would you like to pick: '''))
    print()

    if choice2 not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        wrong_option()

    else:
        # get function from dict and execute
        # if option not found then execute wrong option function
        INPUT_CHOICES.get(choice2, 9)()


if __name__ == '__main__':
    start()
