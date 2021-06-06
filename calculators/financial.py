# Financial code still in progress

import time
import colors
import restart
import math


def payroll():
    weekly = float(input("How much money do you make weekly: "))
    print()

    if weekly <= 0:
        print(
            colors.red + "Please select a valid positive salary, having a salary below or equal to 0 is not possible.",
            colors.reset)
        time.sleep(2)
        payroll()

    else:
        bi_weekly = weekly * 2
        monthly = weekly * 4
        semi_annual = monthly * 6
        annual = monthly * 12
        decade = annual * 10
        print(colors.green + "Weekly Pay:", weekly)
        print(colors.green + "Bi-Weekly Pay:", bi_weekly)
        print(colors.green + "Monthly Pay:", monthly)
        print(colors.green + "Semi-Annual Pay:", semi_annual)
        print(colors.green + "Annual Pay:", annual)
        print(colors.green + "Decade (10 Years) Pay:", decade, '\n', colors.reset)
        time.sleep(1)
        restart.restart()


def tipping():
    total_bill = float(input("How much is your total bill: "))
    print()
    people_number = int(input("How many people: "))

    if total_bill <= 0:
        print(
            colors.red + "Please select a valid positive bill amount, having a bill amount below or equal to 0 is not "
                         "possible.", colors.reset)
        time.sleep(2)
        tipping()

    elif people_number <= 0:
        print(
            colors.red + "Please select a valid positive amount of people, having an amount of people below or equal "
                         "to 0 is not possible.", colors.reset)
        time.sleep(2)
        tipping()

    else:
        five_percent = total_bill * 0.05 / people_number
        ten_percent = total_bill * 0.10 / people_number
        fifteen_percent = total_bill * 0.15 / people_number
        twenty_percent = total_bill * 0.20 / people_number
        twenty_five_percent = total_bill * 0.25 / people_number
        print(colors.green + "5 Percent Tip Per Person:", five_percent)
        print(colors.green + "10 Percent Tip Per Person:", ten_percent)
        print(colors.green + "15 Percent Tip Per Person:", fifteen_percent)
        print(colors.green + "20 Percent Tip Per Person:", twenty_percent)
        print(colors.green + "25 Percent Tip Per Person:", twenty_five_percent, '\n', colors.reset)
        time.sleep(1)
        restart.restart()


def interest():
    principal = float(input("How much money do you currently have in the bank: "))
    rate = float(input("What is your interest rate: "))

    if rate <= 0:
        print(colors.red, 'You cannot have a rate less than or equal to 0!', colors.reset, '\n')
        time.sleep(2)
        interest()

    else:
        years = int(input("Over how many years is the interest compounded: "))

        if years <= 0:
            print(colors.red, 'You cannot have a yearly compound interest timeline that is less than or equal to 0!',
                  colors.reset, '\n')
            time.sleep(2)
            interest()

        else:
            print()
            actual_principal = float(principal)
            actual_rate = float(rate)
            actual_time = int(years)
            A = math.pow((1 + actual_rate), actual_time)
            B = actual_principal * A
            print(colors.green, 'Your Balance After Compound Interest:', B, '\n', colors.reset)
            restart.restart()


def start():
    choice = int(input("""(1) Payroll Calculator
(2) Restaurant Tip Calculator
(3) Compound Interest Calculator
Which calculation would you like to perform: """))
    print()

    if choice == 1:
        payroll()
    elif choice == 2:
        tipping()
    elif choice == 3:
        interest()
    else:
        print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)
        time.sleep(1)
        start()
