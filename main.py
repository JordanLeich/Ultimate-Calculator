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
    6: contribution.start,
    7: restart.restart,
    8: end.end,
    9: wrong_option
}


def start():
    choice = int(input('''
All Calculators and Converters!
(1) Basic Arithmetic Math (Add, Subtract, Multiply, Divide, & More)
(2) Algebra (Find Slope, Pythagorean Theorem)
(3) All Converters (Temperature, Mass, Length, Volume)
(4) Stock Market Shares Calculator
(5) Time Converter (Hours to Days, Days in Years, * More)
(6) All Contributors For This Project 
(7) Restart
(8) Exit
Which calculator would you like to use: '''))
    print()

    # get function from dict and execute
    # if option not found then execute wrong option function
    INPUT_CHOICES.get(choice, 9)()


if __name__ == '__main__':
    start()
