import math
import random
from modules.tools import repeat_input
from modules import colors
from modules.errors import Exit


# Entire operation
def basic_calc():
    history = []
    print("Use '--help' for help")
    while True:
        calculation = input("Your Calculation: ")
        if calculation == "--help":
            print("""
--help: list of commands
--history: past calculations
--exit: return to list of calculators
            """)
        elif calculation == "--history":
            for i in history:
                print(i)
        elif calculation == "--exit":
            break
        else:
            try:
                answer = eval(calculation)
                print(answer)
                history.append(f"{calculation} = {answer}")

            except SyntaxError:
                print("Calculation Error")
                continue


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
        side_a = math.sqrt((side_c * side_c) - (side_b * side_b))

        return side_a

    elif formula == 'b':
        side_a = int(a)
        side_c = int(c)
        side_b = math.sqrt(side_c * side_c - side_a * side_a)

        return side_b

    elif formula == 'c':
        side_a = int(a)
        side_b = int(b)
        side_c = math.sqrt(side_a * side_a + side_b * side_b)

        return side_c


def find_distance(x1, y1, x2, y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
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
    while True:
        choice = int(input('''
(1) Find Slope (Rise Over Run)
(2) Find Slope Intercept (y=mx+b)
(3) Find Pythagorean Theorem
(4) Find The Distance Between Two Points
(5) Find The Midpoint of a Line
(6) Return to list of calculators
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

        elif choice == 2:
            m = repeat_input('What is your M value: ', "Invalid Number...\n", "float")
            x = repeat_input('What is your X value: ', "Invalid Number...\n", "float")
            b = repeat_input('What is your B value: ', "Invalid Number...\n", "float")
            print()
            result = find_slope2(m, x, b)
            print(colors.green + 'Result:', result, '\n', colors.reset)

        elif choice == 3:
            formula = repeat_input('Which side (a, b, c) do you wish to calculate: ',
                                   'Invalid Side...\n',
                                   custom_validation=lambda i: i in ('a', 'b', 'c')
                                   )

            if formula == 'a':
                b = repeat_input('Input the length of side b: ', "Invalid Number...\n", 'float')
                c = repeat_input('Input the length of side c: ', "Invalid Number...\n", 'float')
                print()
                result = find_pythagorean(formula, b=b, c=c)
                print(colors.green + 'The length of side a is:', result, '\n', colors.reset)

            elif formula == 'b':
                a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
                c = repeat_input('Input the length of side c: ', "Invalid Number...\n", 'float')
                print()
                result = find_pythagorean(formula, a=a, c=c)
                print(colors.green + 'The length of side b is:', result, '\n', colors.reset)

            elif formula == 'c':
                a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
                b = repeat_input('Input the length of side b: ', "Invalid Number...\n", 'float')
                print()
                result = find_pythagorean(formula, a=a, b=b)
                print(colors.green + 'The length of side c is:', result, '\n', colors.reset)

        elif choice == 4:
            x1 = repeat_input('x1 Value: ', "Invalid Number...\n", "float")
            y1 = repeat_input('y1 Value: ', "Invalid Number...\n", "float")
            x2 = repeat_input('x2 Value: ', "Invalid Number...\n", "float")
            y2 = repeat_input('y2 Value: ', "Invalid Number...\n", "float")
            print()
            distance = find_distance(x1, y1, x2, y2)
            print(colors.green + "The distance between the two points is", distance, '\n', colors.reset)

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

        elif choice == 6:
            break

        elif choice == 7:
            raise Exit

        else:
            print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)


def payroll():
    weekly = float(repeat_input('How much money do you make weekly: ',
                                'Salary must be above 0',
                                'float',
                                lambda i: float(i) > 0
                                ))

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


def tipping():
    total_bill = float(repeat_input('How much is your total bill: ',
                                    'Bill must be above 0',
                                    'float',
                                    lambda i: float(i) > 0
                                    ))
    people_number = int(repeat_input("How many people: ",
                                     'Number of people must be above 0',
                                     'int',
                                     lambda i: float(i) > 0
                                     ))

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


def interest():
    principal = repeat_input('How much money do you currently have in the bank: ',
                             'Amount of money must be a valid number',
                             'int')
    rate = repeat_input('What is your interest rate: ',
                        'Interest rate must be greater than zero',
                        'float',
                        lambda i: float(i) > 0
                        )
    years = repeat_input('Over how many years is the interest compounded: ',
                         'Number of years must be above 0',
                         'int',
                         lambda i: int(i) > 0
                         )

    print()
    actual_principal = float(principal)
    actual_rate = float(rate)
    actual_time = int(years)

    A = math.pow((1 + actual_rate), actual_time)
    B = actual_principal * A
    print(colors.green, 'Your Balance After Compound Interest:', B, '\n', colors.reset)


def financial():
    while True:
        choice = int(input("""(1) Payroll Calculator
(2) Restaurant Tip Calculator
(3) Compound Interest Calculator
(4) Return to list of calculators

Which calculation would you like to perform: """))
        print()

        if choice == 1:
            payroll()
        elif choice == 2:
            tipping()
        elif choice == 3:
            interest()
        elif choice == 4:
            break
        else:
            print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)


def bmi():
    print(colors.yellow + '''
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. 
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater.\n''', colors.reset)
    cm = int(repeat_input("Height (Centimeters): ", "Invalid Height...\n", "float", lambda i: int(i) > 0))
    kg = int(repeat_input("Weight (Kilograms): ", "Invalid Weight...\n", "float", lambda i: int(i) > 0))
    print()

    formula = kg / (cm * cm) * 10000
    if formula <= 18.5:
        scale = 'Underweight'
    elif 18.6 <= formula <= 24.9:
        scale = 'Normal Weight'
    elif 25 <= formula <= 29.9:
        scale = 'Overweight'
    else:
        scale = 'Obese'
    print(colors.green, 'Your BMI Measurement is:', formula, scale, colors.reset, '\n')


def geometry():
    while True:
        choice = int(input('''(1) Find Area
(2) Find Circumference
(3) Find Perimeter
(4) Find Volume
(5) Return to list of calculations

Which Geometry calculator would you like to use: '''))
        print()

        if choice == 1:
            choice = int(input('''(1) Area of a Rectangle
(2) Area of a Circle

Which Shape would you like to solve the area for: '''))
            print()

            if choice == 1:
                length = float(repeat_input('Length: ', 'Length must be positive', 'float', lambda i: float(i) >= 0))
                width = float(repeat_input('Width: ', 'Width must be positive', 'float', lambda i: float(i) >= 0))
                print()
                area = length * width
                print(colors.green, "Area of a Rectangle:", area, colors.reset, '\n')
            elif choice == 2:
                radius = float(repeat_input('Radius: ', 'Radius must be positive', 'float', lambda i: float(i) >= 0))
                print()
                area = math.pi * radius * radius
                print(colors.green, "Area of a Circle:", area, colors.reset, '\n')
            else:
                print(colors.red + "User input error found...\n", colors.reset)

        elif choice == 2:
            radius = float(repeat_input('Radius: ', 'Radius must be positive', 'float', lambda i: float(i) >= 0))
            print()
            circumference = 2 * math.pi * radius
            print(colors.green, "Circumference:", circumference, colors.reset, '\n')

        elif choice == 3:
            a = float(repeat_input('Length: ', 'Length must be positive', 'float', lambda i: float(i) >= 0))
            b = float(repeat_input('Width: ', 'Width must be positive', 'float', lambda i: float(i) >= 0))
            c = float(repeat_input('Height: ', 'Height must be positive', 'float', lambda i: float(i) >= 0))
            print()
            perimeter = a + b + c
            print(colors.green, "Perimeter:", perimeter, colors.reset, '\n')

        elif choice == 4:
            choice = int(input('''(1) Volume of a Cube
(2) Volume of a Right Rectangular Prism
(3) Volume of a Cylinder

Which Shape would you like to solve the volume for: '''))
            print()

            if choice == 1:
                side = float(repeat_input('Length: ', 'Length must be positive', 'float', lambda i: float(i) >= 0))
                print()
                volume = side * side * side
                print(colors.green, "Volume:", volume, colors.reset, '\n')
            elif choice == 2:
                length = float(repeat_input('Length: ', 'Length must be positive', 'float', lambda i: float(i) >= 0))
                width = float(repeat_input('Width: ', 'Width must be positive', 'float', lambda i: float(i) >= 0))
                height = float(repeat_input('Height: ', 'Height must be positive', 'float', lambda i: float(i) >= 0))
                print()
                volume = length * width * height
                print(colors.green, "Volume:", volume, colors.reset, '\n')
            elif choice == 3:
                area = float(repeat_input('Radius: ', 'Radius must be positive', 'float', lambda i: float(i) >= 0))
                height = float(repeat_input('Height: ', 'Height must be positive', 'float', lambda i: float(i) >= 0))
                print()
                volume = math.pi * area * area * height
                print(colors.green, "Volume:", volume, colors.reset, '\n')
            else:
                print(colors.red + "User input error found...\n", colors.reset)

        elif choice == 5:
            break

        else:
            print(colors.red + "User input error found...\n", colors.reset)


def stocks():
    user_shares = float(repeat_input('Number of Shares: ', 'Must be positive', 'float', lambda i: float(i) > 0))
    user_purchase_price = float(repeat_input('Purchase Price ($): ', 'Must be positive', 'float',
                                             lambda i: float(i) > 0))
    user_sell_price = float(repeat_input('Sell Price ($): ', 'Must be positive', 'float', lambda i: float(i) > 0))
    user_buy_commission = float(repeat_input('Buy Commission (if none, put 0): ',
                                             'Must be positive',
                                             'float',
                                             lambda i: float(i) >= 0
                                             ))
    user_sell_commission = float(repeat_input('Sell Commission (if none, put 0): ',
                                              'Must be positive',
                                              'float',
                                              lambda i: float(i) >= 0))
    print()
    results(user_shares, user_sell_commission, user_buy_commission,
            user_sell_price, user_purchase_price)


def results(user_shares, user_sell_commission, user_buy_commission, user_sell_price, user_purchase_price):
    user_gain_loss = ((user_sell_price * user_shares) - user_sell_commission) - (
            (user_purchase_price * user_shares) + user_buy_commission)

    print(colors.green + 'Profit gain/loss:',
          user_gain_loss, 'Dollars.', colors.reset, '\n')


def random_number():
    start_number = int(repeat_input('Pick a starting number: ', 'Must be a number', 'int'))
    end_number = int(repeat_input('Pick a ending number: ', 'Must be a number', 'int'))
    print()
    number = random.randint(start_number, end_number)
    print(colors.green, 'Your random generated number:', number, '\n', colors.reset)


def heads_or_tails():
    choice = repeat_input('Pick heads or tails: ',
                          'Invalid choice',
                          custom_validation=lambda i: i in ['heads', 'h', 't', 'tails', 'tail', 'head']
                          )

    coin_flip = ['heads', 'tails']
    print('You have picked:', choice)
    print('The coin flip landed on:', random.choice(coin_flip), '\n')


def randomization():
    while True:
        choice = int(input("""(1) Random Number Generator
(2) Heads or Tails 
(3) Exit

Which calculation would you like to perform: """))
        print()

        if choice == 1:
            random_number()
        elif choice == 2:
            heads_or_tails()
        elif choice == 3:
            break
        else:
            print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)


def bitwise():
    # Turns the result from bin into something nice
    nbin = lambda x: bin(x)[2:] if x >= 0 else '-' + bin(x)[3:]
    binary_operators = {'&', '|', '^', '<<', '>>'}
    unary_operators = {'~'}

    operand_1 = int(repeat_input('First number: ', 'Must be an integer', 'int'))
    operator = repeat_input('Operator: ',
                            'Must be a bitwise operator',
                            custom_validation=lambda i: i in binary_operators | unary_operators
                            )

    if operator in binary_operators:
        operand_2 = int(repeat_input('Second number: ', 'Must be an integer', 'int'))
        answer = eval(str(operand_1) + operator + str(operand_2))

        print(f'{operand_1} {operator} {operand_2} = {answer}')
        print(f'{nbin(operand_1)} {operator} {nbin(operand_2)} = {nbin(answer)}')
    else:
        answer = eval(operator + str(operand_1))

        print(f'{operator}{operand_1} = {answer}')
        print(f'{operator}{nbin(operand_1)} = {nbin(answer)}')


def start():
    while True:
        print(colors.green + "All Calculators", colors.reset)
        choice = int(input('''
(1) Basic Calculator     |       (6) Randomization
(2) Algebra              |       (7) Stocks
(3) Geometry             |       (8) Bitwise Operations
(4) Financial            |       (9) Return to main menu
(5) Body Mass Index      |       (10) Quit

Which calculator would you like to use: '''))
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
            bitwise()
        elif choice == 9:
            return
        elif choice == 10:
            raise Exit
        else:
            print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)


if __name__ == '__main__':
    start()
