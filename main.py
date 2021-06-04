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
    print(colors.green + 'All Calculators and Converters!', colors.reset)
    choice = int(input('''(1) Basic Arithmetic Math (Add, Subtract, Multiply, Divide, & More)
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

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 and \
            choice != 8 and choice != 9:
        wrong_option()

    else:
        # get function from dict and execute
        # if option not found then execute wrong option function
        INPUT_CHOICES.get(choice, 9)()


if __name__ == '__main__':
    start()
