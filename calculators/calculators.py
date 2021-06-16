import math
import random
import time
from modules.tools import repeat_input
from math import sqrt
from modules import restart, end, colors


def calculator(data):
    if len(data) <= 3:
        return data[0]

    total: float = 0
    for ind, dta in enumerate(data):
        if dta == "+":
            total += float(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "-":
            total -= float(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "/":
            total /= float(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "*":
            total *= float(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "**":
            total **= float(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "=":
            break

        else:
            total += float(dta)

    return int(total) if total.is_integer() else total


# Entire operation
def basic_calc():
    print(colors.yellow + 'When you are finishing making your arithmetic problem, please use = when asked for an '
                          'operator!\n', colors.reset)
    calculation = []
    while True:
        while True:
            try:
                number = input("Your Number: ")
                float(number)
                calculation.append(number)
                break
            except ValueError:
                print("error")
                continue

        while True:
            operator_options = [
                "+", "-", "*", "/", "**", "=",
                "add", "subtract", "multiply", "times",
                "power", "divide", "division", "equals"]

            operator = input("Your Operator: ")
            if operator in operator_options:
                calculation.append(operator)
                break
            else:
                print(colors.red + "Error Found...\n", colors.reset)
                continue

        if operator == "=":
            print()
            print(colors.green + " ".join(calculation), calculator(calculation), colors.reset)
            break
        print(" ".join(calculation))

    print()
    continue_opt = input("Would you like to make another arithmetic calculation (yes / no): ")
    print()
    if continue_opt.lower() in ['y', 'yes']:
        start()
    elif continue_opt.lower() in ['n', 'no']:
        restart.restart()
    else:
        print(colors.red + 'User input error found...\n', colors.reset)
        time.sleep(2)
        restart.restart()


def find_slope1(y2, y1, x2, x1):
    y2 = float(y2)
    y1 = float(y1)
    x2 = float(x2)
    x1 = float(x1)
    slope = (y2 - y1) / (x2 - x1)

    return slope


def find_slope2(m, x, b):
    m = float(m)
    x = float(x)
    b = float(b)
    y = m * x + b

    return y


def find_pythagorean(formula, a="", b="", c=""):
    if formula == 'a':
        side_b = int(b)
        side_c = int(c)
        side_a = sqrt((side_c * side_c) - (side_b * side_b))

        return side_a

    elif formula == 'b':
        side_a = int(a)
        side_c = int(c)
        side_b = sqrt(side_c * side_c - side_a * side_a)

        return side_b

    elif formula == 'c':
        side_a = int(a)
        side_b = int(b)
        side_c = sqrt(side_a * side_a + side_b * side_b)

        return side_c


def find_distance(x1, y1, x2, y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    distance = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return distance


def find_midpoint(x1, y1, x2, y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    x_m_point = (x1 + x2) / 2
    y_m_point = (y1 + y2) / 2

    return x_m_point, y_m_point


def algebra():
    choice = int(input('''
(1) Find Slope (Rise Over Run)
(2) Find Slope Intercept (y=mx+b)
(3) Find Pythagorean Theorem
(4) Find The Distance Between Two Points
(5) Find The Midpoint of a Line
(6) Restart
(7) Quit

What calculation would you like to perform: '''))
    print()

    if choice == 1:
        float_error = "Invalid Number...\n"
        y2 = repeat_input("What is your Y2 value: ", float_error, "float")
        y1 = repeat_input("What is your Y1 value: ", float_error, "float")
        x2 = repeat_input("What is your X2 value: ", float_error, "float")
        x1 = repeat_input("What is your X1 value: ", float_error, "float")
        print()
        result = find_slope1(y2, y1, x2, x1)
        print(colors.green + 'Slope:', result, '\n', colors.reset)
        restart.restart()

    elif choice == 2:
        m = repeat_input('What is your M value: ', "Invalid Number...\n", "float")
        x = repeat_input('What is your X value: ', "Invalid Number...\n", "float")
        b = repeat_input('What is your B value: ', "Invalid Number...\n", "float")
        print()
        result = find_slope2(m, x, b)
        print(colors.green + 'Result:', result, '\n', colors.reset)
        restart.restart()

    elif choice == 3:
        while True:
            formula = input('Which side (a, b, c) do you wish to calculate: ')
            print()
            if formula in ['a', 'b', 'c']:
                break
            print(colors.red + 'User input error found...\n', colors.reset)

        if formula.lower() == 'a':
            b = repeat_input('Input the length of side b: ', "Invalid Number...\n", 'float')
            c = repeat_input('Input the length of side c: ', "Invalid Number...\n", 'float')
            print()
            result = find_pythagorean(formula, b=b, c=c)
            print(colors.green + 'The length of side a is:', result, '\n', colors.reset)
            restart.restart()

        elif formula.lower() == 'b':
            a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
            c = repeat_input('Input the length of side c: ', "Invalid Number...\n", 'float')
            print()
            result = find_pythagorean(formula, a=a, c=c)
            print(colors.green + 'The length of side b is:', result, '\n', colors.reset)
            restart.restart()

        elif formula.lower() == 'c':
            a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
            b = repeat_input('Input the length of side b: ', "Invalid Number...\n", 'float')
            print()
            result = find_pythagorean(formula, a=a, b=b)
            print(colors.green + 'The length of side c is:', result, '\n', colors.reset)
            restart.restart()

    elif choice == 4:
        x1 = repeat_input('x1 Value: ', "Invalid Number...\n", "float")
        y1 = repeat_input('y1 Value: ', "Invalid Number...\n", "float")
        x2 = repeat_input('x2 Value: ', "Invalid Number...\n", "float")
        y2 = repeat_input('y2 Value: ', "Invalid Number...\n", "float")
        print()
        distance = find_distance(x1, y1, x2, y2)
        print(colors.green + "The distance between the two points is", distance, '\n', colors.reset)
        restart.restart()

    elif choice == 5:
        x1 = repeat_input('The value of x1: ', "Invalid Number...\n", "float")
        y1 = repeat_input('The value of y1: ', "Invalid Number...\n", "float")
        x2 = repeat_input('The value of x2: ', "Invalid Number...\n", "float")
        y2 = repeat_input('The value of y2: ', "Invalid Number...\n", "float")
        print()
        midpoint = find_midpoint(x1, y1, x2, y2)
        x_m_point = midpoint[0]
        y_m_point = midpoint[1]

        print(colors.green + "The midpoint's x value is:", x_m_point)
        print("The midpoint's y value is:", y_m_point, '\n', colors.reset)
        restart.restart()

    elif choice == 6:
        restart.restart()

    elif choice == 7:
        end.end()

    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        start()


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


def financial():
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
        financial()


def bmi():
    print(colors.yellow + '''
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. 
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater.\n''', colors.reset)
    cm = int(repeat_input("Height (Centimeters): ", "Invalid Height...\n", "float"))
    print()
    kg = int(repeat_input("Weight (Kilograms): ", "Invalid Weight...\n", "float"))
    print()
    if cm <= 0:
        print(colors.red + 'Error: Height Must Be More Than 0', colors.reset)
        time.sleep(2)
        bmi()
    elif kg <= 0:
        print(colors.red + 'Error: Weight Must Be More Than 0', colors.reset)
        time.sleep(2)
        bmi()
    formula = kg / (cm * cm) * 10000
    scale = str
    if formula <= 18.5:
        scale = 'Underweight'
    elif 18.6 <= formula <= 24.9:
        scale = 'Normal Weight'
    elif 25 <= formula <= 29.9:
        scale = 'Overweight'
    elif formula >= 30:
        scale = 'Obese'
    print(colors.green, 'Your BMI Measurement is:', formula, scale, colors.reset, '\n')
    time.sleep(1)
    restart.restart()


def geometry():
    choice = int(input('''(1) Find Area
(2) Find Circumference
(3) Find Perimeter
(4) Find Volume

Which Geometry calculator would you like to use: '''))
    print()

    if choice == 1:
        choice = int(input('''(1) Area of a Rectangle
(2) Area of a Circle

Which Shape would you like to solve the area for: '''))
        print()

        if choice == 1:
            length = float(input('Length: '))
            width = float(input('Width: '))
            print()
            area = length * width
            print(colors.green, "Area of a Rectangle:", area, colors.reset, '\n')
            restart.restart()
        elif choice == 2:
            radius = float(input('Radius: '))
            print()
            area = math.pi * radius * radius
            print(colors.green, "Area of a Circle:", area, colors.reset, '\n')
            restart.restart()
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)
            geometry()
    elif choice == 2:
        radius = float(input('Radius: '))
        print()
        circumference = 2 * math.pi * radius
        print(colors.green, "Circumference:", circumference, colors.reset, '\n')
        restart.restart()
    elif choice == 3:
        a = float(input('A: '))
        b = float(input('B: '))
        c = float(input('C: '))
        print()
        perimeter = a + b + c
        print(colors.green, "Perimeter:", perimeter, colors.reset, '\n')
        restart.restart()
    elif choice == 4:
        choice = int(input('''(1) Volume of a Cube
(2) Volume of a Right Rectangular Prism
(3) Volume of a Prism or Cylinder

Which Shape would you like to solve the volume for: '''))
        print()

        if choice == 1:
            side = float(input('Length of the Side: '))
            print()
            volume = side * side * side
            print(colors.green, "Volume:", volume, colors.reset, '\n')
            restart.restart()
        elif choice == 2:
            length = float(input('Length: '))
            width = float(input('Width: '))
            height = float(input('Height: '))
            print()
            volume = length * width * height
            print(colors.green, "Volume:", volume, colors.reset, '\n')
            restart.restart()
        elif choice == 3:
            area = float(input('Area / Base / Radius: '))
            height = float(input('Height: '))
            print()
            volume = math.pi * area * area * height
            print(colors.green, "Volume:", volume, colors.reset, '\n')
            restart.restart()
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)
            geometry()

    else:
        print(colors.red + "User input error found...\n", colors.reset)
        time.sleep(2)
        geometry()


def stocks():
    user_shares = float(input('Number of Shares: '))
    user_purchase_price = float(input('Purchase Price ($): '))
    user_sell_price = float(input('Sell Price ($): '))
    user_buy_commission = float(input('Buy Commission (if none, put 0): '))
    user_sell_commission = float(input('Sell Commission (if none, put 0): '))
    print()
    results(user_shares, user_sell_commission, user_buy_commission,
            user_sell_price, user_purchase_price)


def results(user_shares, user_sell_commission, user_buy_commission, user_sell_price, user_purchase_price):
    user_gain_loss = ((user_sell_price * user_shares) - user_sell_commission) - (
            (user_purchase_price * user_shares) + user_buy_commission)

    print(colors.green + 'Profit gain/loss:',
          user_gain_loss, 'Dollars.', colors.reset, '\n')
    restart.restart()


def random_number():
    start_number = int(input('Pick a starting number: '))
    end_number = int(input('Pick a ending number: '))
    print()
    number = random.randint(start_number, end_number)
    print(colors.green, 'Your random generated number:', number, '\n', colors.reset)
    restart.restart()


def heads_or_tails():
    choice = input('Pick heads or tails: ')
    print()

    if choice.lower() not in ['heads', 'h', 't', 'tails', 'tail', 'head']:
        print(colors.red, 'User input error found! Restarting heads or tails...')
        time.sleep(2)
        heads_or_tails()

    else:
        coin_flip = ['heads', 'tails']
        print('You have picked:', choice)
        print('The coin flip landed on:', random.choice(coin_flip), '\n')
        restart.restart()


def randomization():
    choice = int(input("""(1) Random Number Generator
(2) Heads or Tails 

Which calculation would you like to perform: """))
    print()

    if choice == 1:
        random_number()
    elif choice == 2:
        heads_or_tails()
    else:
        print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)
        time.sleep(1)
        randomization()


def start():
    print(colors.green + "All Calculators", colors.reset)
    choice = int(input('''
(1) Basic Calculator     |       (6) Randomization          
(2) Algebra              |       (7) Stocks         
(3) Geometry             |       (8) Restart       
(4) Financial            |       (9) Quit         
(5) Body Mass Index      |                  

Which convertion would you like to use: '''))
    print()

    if choice == 1:
        basic_calc()
    elif choice == 2:
        algebra()
    elif choice == 3:
        geometry()
    elif choice == 4:
        financial()
    elif choice == 5:
        bmi()
    elif choice == 6:
        randomization()
    elif choice == 7:
        stocks()
    elif choice == 8:
        restart.restart()
    elif choice == 9:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        time.sleep(2)
        start()


if __name__ == '__main__':
    start()
