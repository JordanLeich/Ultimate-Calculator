#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021, all contributors via GitHub can be found at
# https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors

# Imports
import algebra
import calculator
import conversions
import restart
import end
import colors
import stocks
import time_converter
import contribution 
import financial


def wrong_option():
    print(colors.red + 'User input error found... Restarting user input choice...', colors.reset)
    import time
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
    9: end.end,
    10: wrong_option
}


def start():
    choice = int(input('''
All Calculators and Converters!
(1) Basic Arithmetic Math (Add, Subtract, Multiply, Divide, & More)
(2) Algebra (Find Slope, Pythagorean Theorem)
(3) All Converters (Temperature, Mass, Length, Volume)
(4) Stock Market Shares Calculator
(5) Time Converter (Hours to Days, Days in Years, * More)
(6) Financial Calculator (Payroll, Salary, Restaurant Tipping)
(7) All Contributors For This Project 
(8) Restart
(9) Exit
Which calculator would you like to use: '''))
    print()

    # get function from dict and execute
    # if option not found then execute wrong option function
    INPUT_CHOICES.get(choice, 10)()


if __name__ == '__main__':
    start()
