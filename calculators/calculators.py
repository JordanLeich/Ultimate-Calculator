import math
import random
import time

from modules.tools import repeat_input
from modules import colors
from modules.errors import Exit


def basic_calc():
    """
This is the basic arithmetic calculator that handles simply arithmetic equations and outputs the result
    """
    history = []
    print(colors.yellow + "Use '--help' for help\n", colors.reset)
    while True:
        calculation = input("Your Calculation: ")
        print()
        if calculation in ["--help", '--h', 'h', 'help']:
            print("""
--help: list of commands
--history: past calculations
--exit: return to list of calculators
            """)
        elif calculation in ["--history", 'history']:
            for i in history:
                print(i)
        elif calculation in ["--exit", 'e', 'exit']:
            break
        else:
            try:
                answer = eval(calculation)
                print(answer, '\n')
                history.append(f"{calculation} = {answer}")

            except SyntaxError:
                print("Calculation Error")
                continue


def rise_over_run_slope(y2, y1, x2, x1):
    """
Handles the formula used for rise over run format to find slope
    """
    y2 = float(y2)
    y1 = float(y1)
    x2 = float(x2)
    x1 = float(x1)
    return (y2 - y1) / (x2 - x1)


def slope_intercept_form(m, x, b):
    """
Handles the formula used for y=mx+b format to find slope
    """
    m = float(m)
    x = float(x)
    b = float(b)
    return m * x + b


def square_root(number):
    """
function to find square root of number
    """
    return math.sqrt(number)


def square(number):
    """
function to find square of number
    """
    return int(number ** 2)


def sin(number):
    """
function to find sin value of number
    """
    return math.sin(number)


def cos(number):
    """
function to find cos value of number
    """
    return math.cos(number)


def tan(number):
    """
function to find tan value of number
    """
    return math.tan(number)


def find_pythagorean(formula, a="", b="", c=""):
    """
Handles the formula used for pythagorean theorem
    """
    if formula == 'a':
        side_b = int(b)
        side_c = int(c)
        side_a = math.sqrt(side_c ** 2 - side_b ** 2)

        return side_a

    elif formula == 'b':
        side_a = int(a)
        side_c = int(c)
        side_b = math.sqrt(side_c ** 2 - side_a ** 2)

        return side_b

    elif formula == 'c':
        side_a = int(a)
        side_b = int(b)
        side_c = math.sqrt(side_a ** 2 + side_b ** 2)

        return side_c


def find_distance(x1, y1, x2, y2):
    """
Handles the formula used for finding the distance between two graphed points
    """
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def find_midpoint(x1, y1, x2, y2):
    """
Handles the formula used for finding the midpoint between two graphed points
    """
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    x_m_point = (x1 + x2) / 2
    y_m_point = (y1 + y2) / 2

    return x_m_point, y_m_point


def algebra():  # sourcery no-metrics
    """
Entire operation and hub for all algebra related calculators
    """
    while True:
        choice = int(input('''
(1) Find Slope (Rise Over Run)
(2) Find Slope Intercept (y=mx+b)
(3) Find Pythagorean Theorem
(4) Find The Distance Between Two Points
(5) Find The Midpoint of a Line
(6) Find Cos, Sin, or Tan value of a number
(7) Square or Square Root a number
(8) Return to list of calculators
(9) Quit

What calculation would you like to perform: '''))
        print()

        if choice == 1:
            float_error = "Invalid Number...\n"
            y2 = repeat_input("What is your Y2 value: ", float_error, "float")
            y1 = repeat_input("What is your Y1 value: ", float_error, "float")
            x2 = repeat_input("What is your X2 value: ", float_error, "float")
            x1 = repeat_input("What is your X1 value: ", float_error, "float")
            print()
            result = rise_over_run_slope(y2, y1, x2, x1)
            print(colors.green + 'Slope:', result, colors.reset)

        elif choice == 2:
            m = repeat_input('What is your M value: ', "Invalid Number...\n", "float")
            x = repeat_input('What is your X value: ', "Invalid Number...\n", "float")
            b = repeat_input('What is your B value: ', "Invalid Number...\n", "float")
            print()
            result = slope_intercept_form(m, x, b)
            print(colors.green + 'Result:', result, colors.reset)

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
                print(colors.green + 'The length of side a is:', result, colors.reset)

            elif formula == 'b':
                a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
                c = repeat_input('Input the length of side c: ', "Invalid Number...\n", 'float')
                print()
                result = find_pythagorean(formula, a=a, c=c)
                print(colors.green + 'The length of side b is:', result, colors.reset)

            elif formula == 'c':
                a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
                b = repeat_input('Input the length of side b: ', "Invalid Number...\n", 'float')
                print()
                result = find_pythagorean(formula, a=a, b=b)
                print(colors.green + 'The length of side c is:', result, colors.reset)

        elif choice == 4:
            x1 = repeat_input('x1 Value: ', "Invalid Number...\n", "float")
            y1 = repeat_input('y1 Value: ', "Invalid Number...\n", "float")
            x2 = repeat_input('x2 Value: ', "Invalid Number...\n", "float")
            y2 = repeat_input('y2 Value: ', "Invalid Number...\n", "float")
            print()
            distance = find_distance(x1, y1, x2, y2)
            print(colors.green + "The distance between the two points is", distance, colors.reset)

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
            print("The midpoint's y value is:", y_m_point, colors.reset)

        elif choice == 6:
            choice = int(input('''(1) Find Sin value
(2) Find Cos value
(3) Find Tan value
(4) Return to list of calculators
(5) Quit

Which option would you like to pick: '''))
            print()

            if choice == 1:
                number = float(input('Enter a number you would like to find the Sin value for: '))
                print()
                print(colors.green, sin(number), colors.reset)
            elif choice == 2:
                number = float(input('Enter a number you would like to find the Cos value for: '))
                print()
                print(colors.green, cos(number), colors.reset)
            elif choice == 3:
                number = float(input('Enter a number you would like to find the Tan value for: '))
                print()
                print(colors.green, tan(number), colors.reset)
            elif choice == 4:
                return
            elif choice == 5:
                raise Exit
            else:
                print(colors.red + 'User input error found...\n', colors.reset)
                time.sleep(2)

        elif choice == 7:
            choice = int(input('''(1) Square a number
(2) Square Root a number
(3) Return to list of calculators
(4) Exit 

Which option would you like to pick: '''))
            print()

            if choice == 1:
                number = float(input('Enter a number you would like to find the square of: '))
                print()
                print(colors.green, square(number), colors.reset)
            elif choice == 2:
                number = float(input('Enter a number you would like to find the square root of: '))
                print()
                print(colors.green, square_root(number), colors.reset)
            elif choice == 3:
                return
            elif choice == 4:
                raise Exit
            else:
                print(colors.red + 'User input error found...\n', colors.reset)
                time.sleep(2)
        elif choice == 8:
            break
        elif choice == 9:
            raise Exit
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)


def payroll():
    """
Used under the financial calculator, this function determines how much money you will make in a given set of time
    """
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
    """
Used under the financial calculator, this function determines how much money to tip given a set total bill and amount
of people
    """
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
    print()

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
    """
Used under the financial calculator, this function determines how much money is gained or lost from an interest rate
    """
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


def discount():
    list_price = float(input('List price: '))
    print()
    sale_price = float(input('Sale price: '))
    print()
    discount_percent = sale_price / list_price * 100
    discount_amount = list_price - sale_price
    print(colors.green, 'Discount percent:', str(discount_percent) + '% Off. Discount amount:', discount_amount,
          'Dollars.\n', colors.reset)


def sale_price_calculator():
    list_price = float(input('List price: '))
    print()
    discount_percent = float(input('Discount percent: '))
    print()
    sale_price = discount_percent / list_price * 100
    discount_amount = list_price - sale_price
    print(colors.green, 'Sale price:', str(sale_price) + '% Off. Discount amount:', discount_amount,
          'Dollars.\n', colors.reset)


def financial():
    """
Main hub for all financial calculator options
    """
    while True:
        choice = int(input("""(1) Payroll Calculator
(2) Restaurant Tip Calculator
(3) Compound Interest Calculator
(4) Discount Calculator
(5) Sale Price Calculator
(6) Return to list of calculators
(7) Exit

Which calculation would you like to perform: """))
        print()

        if choice == 1:
            payroll()
        elif choice == 2:
            tipping()
        elif choice == 3:
            interest()
        elif choice == 4:
            discount()
        elif choice == 5:
            sale_price_calculator()
        elif choice == 6:
            break
        elif choice == 7:
            raise Exit
        else:
            print(colors.red + "User input error found... Restarting user input choice...\n", colors.reset)
            time.sleep(2)


def life_expectancy():
    # sourcery skip: collection-into-set, extract-duplicate-method
    gender = str(input('Male or Female: '))
    print()

    if gender.lower() in ['male', 'm']:
        average_male = 76.3
        smoke = str(input('Do you smoke anything (yes / no): '))
        print()
        if smoke in ['y', 'yes']:
            average_male -= 15
        drink = str(input('Do you drink alcohol (yes / no): '))
        print()
        if drink in ['y', 'yes']:
            average_male -= 5
        print(colors.green, 'Your average life expectancy is about:', average_male, 'years old.\n', colors.reset)
    elif gender.lower() in ['female', 'f']:
        average_female = 81.1
        smoke = str(input('Do you smoke anything (yes / no): '))
        print()
        if smoke in ['y', 'yes']:
            average_female -= 15
        drink = str(input('Do you drink alcohol (yes / no): '))
        print()
        if drink in ['y', 'yes']:
            average_female -= 5
        print(colors.green, 'Your average life expectancy is about:', average_female, 'years old.\n', colors.reset)
    else:
        print(colors.red + 'User input error found...\n', colors.reset)
        time.sleep(2)


def percentage():
    """
Used to find a percentage when given 2 numbers. For example, what is a 1 out of 5 chance, this will give you a 20
percent chance
    """
    print(colors.yellow + 'Used to find a percentage when given 2 numbers. For example, what is a 1 out of 5 chance, '
                          'this will give you a 20 percent chance.\n', colors.reset)
    first_number = float(input('First number: '))
    print()
    second_number = float(input('Second number: '))
    print()
    percentage_result = first_number / second_number * 100
    print(colors.green, str(percentage_result) + '% Percent\n', colors.reset)


def health():
    """
Handles all calculators regarding health such as bmi and life expectancy
    """
    choice = int(input('''(1) BMI (Body Mass Index)
(2) Life Expectancy

Which Health calculator would you like to use? '''))
    print()
    if choice == 1:
        bmi()
    elif choice == 2:
        life_expectancy()
    else:
        print(colors.red + 'User input error found...\n', colors.reset)


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

    formula = kg / cm ** 2 * 10000
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
    """
Main hub for all geometry related calculator options
    """
    while True:
        choice = int(input('''(1) Find Area
(2) Find Circumference
(3) Find Perimeter
(4) Find Volume
(5) Return to list of calculators
(6) Exit

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
                volume = side ** 2 * side
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
        elif choice == 6:
            raise Exit
        else:
            print(colors.red + "User input error found...\n", colors.reset)


def stocks():
    """
Handles all stock evaluations to help predict a gain/loss amount
    """
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
    """
Handles the main formula used to find gain/loss in the stocks function
    """
    user_gain_loss = ((user_sell_price * user_shares) - user_sell_commission) - (
            (user_purchase_price * user_shares) + user_buy_commission)

    print(colors.green + 'Profit gain/loss:',
          user_gain_loss, 'Dollars.', colors.reset, '\n')


def random_number():
    """
Basic function that returns a random integer between two sets of boundary integers, used in the randomization function
    """
    start_number = int(repeat_input('Pick a starting number: ', 'Must be a number', 'int'))
    end_number = int(repeat_input('Pick a ending number: ', 'Must be a number', 'int'))
    print()
    number = random.randint(start_number, end_number)
    print(colors.green, 'Your random generated number:', number, '\n', colors.reset)


def heads_or_tails():
    """
Small game of heads or tails used in the randomization function
    """
    choice = repeat_input('Pick heads or tails: ',
                          'Invalid choice',
                          custom_validation=lambda i: i in ['heads', 'h', 't', 'tails', 'tail', 'head']
                          )

    coin_flip = ['heads', 'tails']
    print('You have picked:', choice)
    print('The coin flip landed on:', random.choice(coin_flip), '\n')


def randomization():
    """
Main hub for all randomization calculators/games
    """
    while True:
        choice = int(input("""(1) Random Number Generator
(2) Heads or Tails 
(3) Return to list of calculators
(4) Exit

Which calculation would you like to perform: """))
        print()

        if choice == 1:
            random_number()
        elif choice == 2:
            heads_or_tails()
        elif choice == 3:
            break
        elif choice == 4:
            raise Exit
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)


def bitwise():
    """
Turns the result from bin into something nice
    """
    bin_number = lambda x: bin_number(x)[2:] if x >= 0 else '-' + bin_number(x)[3:]
    binary_operators = {'&', '|', '^', '<<', '>>'}
    unary_operators = {'~'}

    operand_1 = int(repeat_input('First number: ', 'Must be an integer', 'int'))
    operator = repeat_input('Operator (&, |, ^, <<, or >>): ',
                            'Must be a bitwise operator',
                            custom_validation=lambda i: i in binary_operators | unary_operators
                            )

    if operator in binary_operators:
        operand_2 = int(repeat_input('Second number: ', 'Must be an integer', 'int'))
        answer = eval(str(operand_1) + operator + str(operand_2))

        print(f'{operand_1} {operator} {operand_2} = {answer}')
        print(f'{bin_number(operand_1)} {operator} {bin_number(operand_2)} = {bin_number(answer)}')
    else:
        answer = eval(operator + str(operand_1))

        print(f'{operator}{operand_1} = {answer}')
        print(f'{operator}{bin_number(operand_1)} = {bin_number(answer)}')


def gaming():
    """
Main calculator used for everything gaming related
    """
    while True:
        choice = int(input('''(1) KD (Kill Death) ratio
(2) KDA (Kill Death Assist) ratio
(3) Win/Loss ratio
(4) Return to list of calculators
(5) Exit
    
Which option would you like to pick: '''))
        print()

        if choice == 1:
            kills = int(input('Total kills: '))
            print()
            deaths = int(input('Total deaths: '))
            print()
            kd = kills / deaths
            if kd == 1.0:
                print(colors.yellow + 'Your KD ratio is ' + str(kd), 'This ratio is average in gaming.\n', colors.reset)
            elif kd < 1.0:
                print(colors.red + 'Your KD ratio is ' + str(kd), 'This ratio is below average in gaming.\n',
                      colors.reset)
            elif kd > 1.0:
                print(colors.green + 'Your KD ratio is ' + str(kd), 'This ratio is above average in gaming.\n',
                      colors.reset)
            else:
                print(colors.red + 'User input error found...\n', colors.reset)
                time.sleep(2)
        elif choice == 2:
            kills = int(input('Total kills: '))
            print()
            deaths = int(input('Total deaths: '))
            print()
            assists = int(input('Total assists: '))
            print()
            kda = (kills + assists) / deaths
            if kda == 1.0:
                print(colors.yellow + 'Your KDA ratio is ' + str(kda), 'This ratio is average in gaming.\n',
                      colors.reset)
            elif kda < 1.0:
                print(colors.red + 'Your KDA ratio is ' + str(kda), 'This ratio is below average in gaming.\n',
                      colors.reset)
            elif kda > 1.0:
                print(colors.green + 'Your KDA ratio is ' + str(kda), 'This ratio is above average in gaming.\n',
                      colors.reset)
            else:
                print(colors.red + 'User input error found...\n', colors.reset)
                time.sleep(2)
        elif choice == 3:
            wins = int(input('Total wins: '))
            print()
            loses = int(input('Total loses: '))
            print()
            win_loss_ratio = wins / loses
            if win_loss_ratio == 1.0:
                print(colors.yellow + 'Your Win/Loss ratio is ' + str(win_loss_ratio),
                      'This ratio is average in gaming.\n', colors.reset)
            elif win_loss_ratio < 1.0:
                print(colors.red + 'Your Win/Loss ratio is ' + str(win_loss_ratio),
                      'This ratio is below average in gaming.\n', colors.reset)
            elif win_loss_ratio > 1.0:
                print(colors.green + 'Your Win/Loss ratio is ' + str(win_loss_ratio),
                      'This ratio is above average in gaming.\n', colors.reset)
            else:
                print(colors.red + 'User input error found...\n', colors.reset)
                time.sleep(2)
        elif choice == 4:
            break
        elif choice == 5:
            raise Exit
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)


def download_time():
    """
Used to calculate the download time for a file size being downloaded.
    """
    download_speed = float
    print(colors.yellow + '---Important notes about this calculator---\n')
    time.sleep(1)
    print(
        'Please keep in mind that the download time calculator will give you only an estimate of how long it will take to download something. Given that most peoples download speeds cannot be given a single value but rather an average, no estimate of download time can be 100 percent accurate. To provide the best accuracy with timing, we ask to give an average of your overall download speed.\n')
    time.sleep(1)
    print(
        'If your download size is in Gigabytes, just convert that value to Megabytes. Every 1000 Mb equals a Gb, for example, if you have a download size of 23 Gb, then your download size would 23000 in Mb.\n',
        colors.reset)
    time.sleep(1)
    file_size = int(input('''(1) Megabytes

Select which file size type the download is: '''))
    print()

    if file_size == 1:
        file_size = float(input('How many total megabytes is your download: '))
        print()
        print(
            colors.yellow + 'If you are unsure what your average download/upload speeds are, please go to https://www.speedtest.net/ to find out more.\n',
            colors.reset)
        time.sleep(1)
        download_speed = float(input('How many megabytes per second on average is your download speed: '))
        print()
    else:
        print(colors.red + 'User input error found...\n', colors.reset)
        time.sleep(2)
    download_time_in_seconds = file_size / (download_speed / 8)
    print(colors.green + str(download_time_in_seconds), 'Seconds.')
    download_time_in_minutes = download_time_in_seconds / 60
    print(str(download_time_in_minutes), 'Minutes.')
    download_time_in_hours = download_time_in_minutes / 60
    print(str(download_time_in_hours), 'Hours.\n', colors.reset)

import random

# Function to simulate a coin flip
def coin_flip():
    return random.choice(["Heads", "Tails"])

def probability_calculator():
    # Option to calculate probability or simulate coin flips
    choice = int(input("Calculate the probability of something (1) or simulate the probability of coin flips (2): "))

    if choice == 1:
        # Get user input for total outcomes and successful outcomes
        while True:
            try:
                total_outcomes = int(input("Enter the total number of possible outcomes: "))
                successful_outcomes = int(input("Enter the number of successful outcomes: "))
                if total_outcomes > 0 and successful_outcomes >= 0 and successful_outcomes <= total_outcomes:
                    break
                else:
                    print("Please enter valid input.")
            except ValueError:
                print("Invalid input. Please enter integers.")

        # Calculate the probability
        probability = successful_outcomes / total_outcomes

        # Print the result
        print(f"The probability of success is: {probability:.2f}\n")

    elif choice == 2:
        # Get the number of coin flips as an integer
        while True:
            try:
                num_flips = int(input("Number of coin flips (higher numbers result in longer waiting times): "))
                if num_flips > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        heads_count = 0
        tails_count = 0

        for _ in range(num_flips):
            result = coin_flip()
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1

        # Calculate the probabilities
        probability_heads = heads_count / num_flips
        probability_tails = tails_count / num_flips

        # Print the results
        print(f"Number of Heads: {heads_count}")
        print(f"Number of Tails: {tails_count}")
        print(f"Probability of Heads: {probability_heads:.2f}")
        print(f"Probability of Tails: {probability_tails:.2f}\n")

    else:
        print("Invalid choice. Please select 1 or 2.\n")

def start():
    """
Main hub UI that displays all of the calculators in the project
    """
    while True:
        print(colors.green + "All Calculators", colors.reset)
        choice = int(input('''
(1) Basic Calculator     |       (6) Randomization       |       (11) Download Time
(2) Algebra              |       (7) Stocks              |       (12) Probability
(3) Geometry             |       (8) Bitwise Operations  |       (13) Main Menu
(4) Financial            |       (9) Percentage          |       (14) Exit
(5) Health               |       (10) Gaming

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
            health()
        elif choice == 6:
            randomization()
        elif choice == 7:
            stocks()
        elif choice == 8:
            bitwise()
        elif choice == 9:
            percentage()
        elif choice == 10:
            gaming()
        elif choice == 11:
            download_time()
        elif choice == 12:
            probability_calculator()
        elif choice == 13:
            return
        elif choice == 14:
            raise Exit
        else:
            print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)


if __name__ == '__main__':
    start()
