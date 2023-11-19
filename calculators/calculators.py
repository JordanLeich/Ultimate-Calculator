import math
import statistics
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from modules.tools import repeat_input
from modules import colors
from modules.errors import Exit
from scipy.stats import skew, kurtosis
from collections import Counter
import re


def stats():
    try:
        input_string = input("Enter a list of numbers separated by spaces: ")

        # Split on both spaces and commas
        num_list = [float(x) for x in re.split(r"[,\s]+", input_string)]
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")
        return

    # Calculate mean
    mean = statistics.mean(num_list)

    # Calculate median
    median = statistics.median(num_list)

    # Calculate mode
    num_counts = Counter(num_list)
    mode_count = max(num_counts.values())
    modes = [num for num, count in num_counts.items() if count == mode_count]
    mode = modes if len(modes) > 1 else modes[0]

    # Calculate range
    num_list.sort()
    min_val = num_list[0]
    max_val = num_list[-1]
    data_range = max_val - min_val

    # Calculate quartiles (Q1 and Q3)
    q1 = statistics.median(num_list[: len(num_list) // 2])
    q3 = statistics.median(num_list[(len(num_list) + 1) // 2 :])

    # Calculate interquartile range (IQR)
    iqr = q3 - q1

    # Calculate minimum and maximum
    minimum = min(num_list)
    maximum = max(num_list)

    # Calculate standard deviation
    stdev = statistics.stdev(num_list)

    # Calculate variance
    variance = statistics.variance(num_list)

    # Calculate coefficient of variation (CV)
    cv = (stdev / mean) * 100

    # Calculate skewness and kurtosis
    skewness = skew(num_list)
    kurt = kurtosis(num_list)

    # Plot Histogram
    plt.hist(num_list, bins=10, edgecolor="k")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

    # Plot Box Plot
    plt.boxplot(num_list)
    plt.ylabel("Value")
    plt.title("Box Plot")
    plt.show()

    # Print the results
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Range:", data_range)
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Standard Deviation:", stdev)
    print("Variance:", variance)
    print("Coefficient of Variation (CV):", cv)
    print("Skewness:", skewness)
    print("Kurtosis:", kurt, "\n")


def basic_calc():
    """
    This is the basic arithmetic calculator that handles simple arithmetic equations and outputs the result.
    """
    history = []
    print(colors.yellow + "Use '--help' for help\n", colors.reset)
    while True:
        calculation = input("Your Calculation: ")
        print()
        if calculation in ["--help", "--h", "h", "help"]:
            print(
                """
--help: list of commands
--history: past calculations
--exit: return to the list of calculators
            """
            )
        elif calculation in ["--history", "history"]:
            for i in history:
                print(i)
        elif calculation in ["--exit", "e", "exit"]:
            break
        else:
            try:
                answer = eval(calculation)
                print(answer, "\n")
                history.append(f"{calculation} = {answer}")

            except SyntaxError:
                print("Calculation Error\n")
                continue


def rise_over_run_slope(y2, y1, x2, x1):
    """
    Handles the formula used for rise over run format to find slope
    """
    try:
        y2 = float(y2)
        y1 = float(y1)
        x2 = float(x2)
        x1 = float(x1)
        return (y2 - y1) / (x2 - x1)
    except ValueError:
        return "Invalid input. Please enter numeric values for coordinates."


def slope_intercept_form(m, x, b):
    """
    Handles the formula used for y=mx+b format to find slope
    """
    try:
        m = float(m)
        x = float(x)
        b = float(b)
        return m * x + b
    except ValueError:
        return "Invalid input. Please enter numeric values for m, x, and b."


def square_root(number):
    """
    Function to find the square root of a number
    """
    try:
        number = float(number)
        if number < 0:
            return "Invalid input. Square root is undefined for negative numbers."
        return math.sqrt(number)
    except ValueError:
        return "Invalid input. Please enter a numeric value."


def square(number):
    """
    Function to find the square of a number
    """
    try:
        number = float(number)
        return number**2
    except ValueError:
        return "Invalid input. Please enter a numeric value."


def sin(number):
    """
    Function to find the sine value of a number
    """
    try:
        number = float(number)
        return math.sin(number)
    except ValueError:
        return "Invalid input. Please enter a numeric value."


def cos(number):
    """
    Function to find the cosine value of a number
    """
    try:
        number = float(number)
        return math.cos(number)
    except ValueError:
        return "Invalid input. Please enter a numeric value."


def tan(number):
    """
    Function to find the tangent value of a number
    """
    try:
        number = float(number)
        return math.tan(number)
    except ValueError:
        return "Invalid input. Please enter a numeric value."


def find_pythagorean(formula, a="", b="", c=""):
    """
    Handles the formula used for the Pythagorean theorem
    """
    try:
        if formula == "a":
            side_b = float(b)
            side_c = float(c)
            side_a = math.sqrt(side_c**2 - side_b**2)
            return side_a

        elif formula == "b":
            side_a = float(a)
            side_c = float(c)
            side_b = math.sqrt(side_c**2 - side_a**2)
            return side_b

        elif formula == "c":
            side_a = float(a)
            side_b = float(b)
            side_c = math.sqrt(side_a**2 + side_b**2)
            return side_c
        else:
            return "Invalid input. Please enter 'a', 'b', or 'c' for the Pythagorean theorem formula."
    except ValueError:
        return "Invalid input. Please enter numeric values for the sides."


def find_distance(x1, y1, x2, y2):
    """
    Handles the formula used for finding the distance between two graphed points
    """
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    except ValueError:
        return "Invalid input. Please enter numeric values for coordinates."


def find_midpoint(x1, y1, x2, y2):
    """
    Handles the formula used for finding the midpoint between two graphed points
    """
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)

        x_m_point = (x1 + x2) / 2
        y_m_point = (y1 + y2) / 2

        return x_m_point, y_m_point
    except ValueError:
        return "Invalid input. Please enter numeric values for coordinates."


def graphing():
    # Get user input for m and b
    try:
        m = float(input("Enter the value of m: "))
        b = float(input("Enter the value of b: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for m and b.")
        exit(1)

    # Generate x values
    x = np.linspace(-10, 10, 400)  # You can adjust the range of x-values as needed

    # Calculate y values based on the linear equation y = mx + b
    y = m * x + b

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {m}x + {b}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Equation Plot")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(color="gray", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.show()


def algebra():  # sourcery no-metrics
    """
    Entire operation and hub for all algebra related calculators
    """
    while True:
        choice = int(
            input(
                """
(1) Find Slope (Rise Over Run)
(2) Find Slope Intercept (y=mx+b)
(3) Find Pythagorean Theorem
(4) Find The Distance Between Two Points
(5) Find The Midpoint of a Line
(6) Find Cos, Sin, or Tan value of a number
(7) Square or Square Root a number
(8) Create a graph (y=mx+b)                           
(9) Return to list of calculators
(10) Quit

What calculation would you like to perform: """
            )
        )
        print()

        if choice == 1:
            float_error = "Invalid Number...\n"
            y2 = repeat_input("What is your Y2 value: ", float_error, "float")
            y1 = repeat_input("What is your Y1 value: ", float_error, "float")
            x2 = repeat_input("What is your X2 value: ", float_error, "float")
            x1 = repeat_input("What is your X1 value: ", float_error, "float")
            print()
            result = rise_over_run_slope(y2, y1, x2, x1)
            print(colors.green + "Slope:", result, colors.reset)

        elif choice == 2:
            m = repeat_input("What is your M value: ", "Invalid Number...\n", "float")
            x = repeat_input("What is your X value: ", "Invalid Number...\n", "float")
            b = repeat_input("What is your B value: ", "Invalid Number...\n", "float")
            print()
            result = slope_intercept_form(m, x, b)
            print(colors.green + "Result:", result, colors.reset)

        elif choice == 3:
            formula = repeat_input(
                "Which side (a, b, c) do you wish to calculate: ",
                "Invalid Side...\n",
                custom_validation=lambda i: i in ("a", "b", "c"),
            )

            if formula == "a":
                b = repeat_input(
                    "Input the length of side b: ", "Invalid Number...\n", "float"
                )
                c = repeat_input(
                    "Input the length of side c: ", "Invalid Number...\n", "float"
                )
                print()
                result = find_pythagorean(formula, b=b, c=c)
                print(colors.green + "The length of side a is:", result, colors.reset)

            elif formula == "b":
                a = repeat_input(
                    "Input the length of side a: ", "Invalid Number...\n", "float"
                )
                c = repeat_input(
                    "Input the length of side c: ", "Invalid Number...\n", "float"
                )
                print()
                result = find_pythagorean(formula, a=a, c=c)
                print(colors.green + "The length of side b is:", result, colors.reset)

            elif formula == "c":
                a = repeat_input(
                    "Input the length of side a: ", "Invalid Number...\n", "float"
                )
                b = repeat_input(
                    "Input the length of side b: ", "Invalid Number...\n", "float"
                )
                print()
                result = find_pythagorean(formula, a=a, b=b)
                print(colors.green + "The length of side c is:", result, colors.reset)

        elif choice == 4:
            x1 = repeat_input("x1 Value: ", "Invalid Number...\n", "float")
            y1 = repeat_input("y1 Value: ", "Invalid Number...\n", "float")
            x2 = repeat_input("x2 Value: ", "Invalid Number...\n", "float")
            y2 = repeat_input("y2 Value: ", "Invalid Number...\n", "float")
            print()
            distance = find_distance(x1, y1, x2, y2)
            print(
                colors.green + "The distance between the two points is",
                distance,
                colors.reset,
            )

        elif choice == 5:
            x1 = repeat_input("The value of x1: ", "Invalid Number...\n", "float")
            y1 = repeat_input("The value of y1: ", "Invalid Number...\n", "float")
            x2 = repeat_input("The value of x2: ", "Invalid Number...\n", "float")
            y2 = repeat_input("The value of y2: ", "Invalid Number...\n", "float")
            print()
            midpoint = find_midpoint(x1, y1, x2, y2)
            x_m_point = midpoint[0]
            y_m_point = midpoint[1]

            print(colors.green + "The midpoint's x value is:", x_m_point)
            print("The midpoint's y value is:", y_m_point, colors.reset)

        elif choice == 6:
            choice = int(
                input(
                    """(1) Find Sin value
(2) Find Cos value
(3) Find Tan value
(4) Return to list of calculators
(5) Quit

Which option would you like to pick: """
                )
            )
            print()

            if choice == 1:
                number = float(
                    input("Enter a number you would like to find the Sin value for: ")
                )
                print()
                print(colors.green, sin(number), colors.reset)
            elif choice == 2:
                number = float(
                    input("Enter a number you would like to find the Cos value for: ")
                )
                print()
                print(colors.green, cos(number), colors.reset)
            elif choice == 3:
                number = float(
                    input("Enter a number you would like to find the Tan value for: ")
                )
                print()
                print(colors.green, tan(number), colors.reset)
            elif choice == 4:
                return
            elif choice == 5:
                raise Exit
            else:
                print(colors.red + "User input error found...\n", colors.reset)
                time.sleep(2)

        elif choice == 7:
            choice = int(
                input(
                    """(1) Square a number
(2) Square Root a number
(3) Return to list of calculators
(4) Exit 

Which option would you like to pick: """
                )
            )
            print()

            if choice == 1:
                number = float(
                    input("Enter a number you would like to find the square of: ")
                )
                print()
                print(colors.green, square(number), colors.reset)
            elif choice == 2:
                number = float(
                    input("Enter a number you would like to find the square root of: ")
                )
                print()
                print(colors.green, square_root(number), colors.reset)
            elif choice == 3:
                return
            elif choice == 4:
                raise Exit
            else:
                print(colors.red + "User input error found...\n", colors.reset)
                time.sleep(2)
        elif choice == 8:
            graphing()
        elif choice == 9:
            break
        elif choice == 10:
            raise Exit
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)


def payroll():
    """
    Used under the financial calculator, this function determines how much money you will make in a given set of time
    """
    weekly = float(
        repeat_input(
            "How much money do you make weekly: ",
            "Salary must be above 0",
            "float",
            lambda i: float(i) > 0,
        )
    )

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
    print(colors.green + "Decade (10 Years) Pay:", decade, "\n", colors.reset)


def tipping():
    """
    Used under the financial calculator, this function determines how much money to tip given a set total bill and amount
    of people
    """
    total_bill = float(
        repeat_input(
            "How much is your total bill: ",
            "Bill must be above 0",
            "float",
            lambda i: float(i) > 0,
        )
    )
    people_number = int(
        repeat_input(
            "How many people: ",
            "Number of people must be above 0",
            "int",
            lambda i: float(i) > 0,
        )
    )
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
    print(
        colors.green + "25 Percent Tip Per Person:",
        twenty_five_percent,
        "\n",
        colors.reset,
    )


def interest():
    """
    Used under the financial calculator, this function determines how much money is gained or lost from an interest rate
    """
    principal = repeat_input(
        "How much money do you currently have in the bank: ",
        "Amount of money must be a valid number",
        "int",
    )
    rate = repeat_input(
        "What is your interest rate: ",
        "Interest rate must be greater than zero",
        "float",
        lambda i: float(i) > 0,
    )
    years = repeat_input(
        "Over how many years is the interest compounded: ",
        "Number of years must be above 0",
        "int",
        lambda i: int(i) > 0,
    )

    print()
    actual_principal = float(principal)
    actual_rate = float(rate)
    actual_time = int(years)

    A = math.pow((1 + actual_rate), actual_time)
    B = actual_principal * A
    print(colors.green, "Your Balance After Compound Interest:", B, "\n", colors.reset)


def discount():
    list_price = float(input("List price: "))
    print()
    sale_price = float(input("Sale price: "))
    print()
    discount_percent = sale_price / list_price * 100
    discount_amount = list_price - sale_price
    print(
        colors.green,
        "Discount percent:",
        str(discount_percent) + "% Off. Discount amount:",
        discount_amount,
        "Dollars.\n",
        colors.reset,
    )


def sale_price_calculator():
    list_price = float(input("List price: "))
    print()
    discount_percent = float(input("Discount percent: "))
    print()
    sale_price = discount_percent / list_price * 100
    discount_amount = list_price - sale_price
    print(
        colors.green,
        "Sale price:",
        str(sale_price) + "% Off. Discount amount:",
        discount_amount,
        "Dollars.\n",
        colors.reset,
    )


def financial():
    """
    Main hub for all financial calculator options
    """
    while True:
        choice = int(
            input(
                """(1) Payroll Calculator
(2) Restaurant Tip Calculator
(3) Compound Interest Calculator
(4) Discount Calculator
(5) Sale Price Calculator
(6) Return to list of calculators
(7) Exit

Which calculation would you like to perform: """
            )
        )
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
            print(
                colors.red
                + "User input error found... Restarting user input choice...\n",
                colors.reset,
            )
            time.sleep(2)


def life_expectancy():
    # sourcery skip: collection-into-set, extract-duplicate-method
    gender = str(input("Male or Female: "))
    print()

    if gender.lower() in ["male", "m"]:
        average_male = 76.3
        smoke = str(input("Do you smoke anything (yes / no): "))
        print()
        if smoke in ["y", "yes"]:
            average_male -= 15
        drink = str(input("Do you drink alcohol (yes / no): "))
        print()
        if drink in ["y", "yes"]:
            average_male -= 5
        print(
            colors.green,
            "Your average life expectancy is about:",
            average_male,
            "years old.\n",
            colors.reset,
        )
    elif gender.lower() in ["female", "f"]:
        average_female = 81.1
        smoke = str(input("Do you smoke anything (yes / no): "))
        print()
        if smoke in ["y", "yes"]:
            average_female -= 15
        drink = str(input("Do you drink alcohol (yes / no): "))
        print()
        if drink in ["y", "yes"]:
            average_female -= 5
        print(
            colors.green,
            "Your average life expectancy is about:",
            average_female,
            "years old.\n",
            colors.reset,
        )
    else:
        print(colors.red + "User input error found...\n", colors.reset)
        time.sleep(2)


def percentage():
    """
    Used to find a percentage when given 2 numbers. For example, what is a 1 out of 5 chance, this will give you a 20
    percent chance
    """
    print(
        colors.yellow
        + "Used to find a percentage when given 2 numbers. For example, what is a 1 out of 5 chance, "
        "this will give you a 20 percent chance.\n",
        colors.reset,
    )
    first_number = float(input("First number: "))
    print()
    second_number = float(input("Second number: "))
    print()
    percentage_result = first_number / second_number * 100
    print(colors.green, str(percentage_result) + "% Percent\n", colors.reset)


def health():
    """
    Handles all calculators regarding health such as bmi and life expectancy
    """
    choice = int(
        input(
            """(1) BMI (Body Mass Index)
(2) Life Expectancy

Which Health calculator would you like to use? """
        )
    )
    print()
    if choice == 1:
        bmi()
    elif choice == 2:
        life_expectancy()
    else:
        print(colors.red + "User input error found...\n", colors.reset)


def bmi():
    print(
        colors.yellow
        + """
    Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. 
    Underweight = <18.5
    Normal weight = 18.5–24.9
    Overweight = 25–29.9
    Obesity = BMI of 30 or greater.\n""",
        colors.reset,
    )
    cm = int(
        repeat_input(
            "Height (Centimeters): ",
            "Invalid Height...\n",
            "float",
            lambda i: int(i) > 0,
        )
    )
    kg = int(
        repeat_input(
            "Weight (Kilograms): ", "Invalid Weight...\n", "float", lambda i: int(i) > 0
        )
    )
    print()

    formula = kg / cm**2 * 10000
    if formula <= 18.5:
        scale = "Underweight"
    elif 18.6 <= formula <= 24.9:
        scale = "Normal Weight"
    elif 25 <= formula <= 29.9:
        scale = "Overweight"
    else:
        scale = "Obese"
    print(colors.green, "Your BMI Measurement is:", formula, scale, colors.reset, "\n")


def geometry():
    """
    Main hub for all geometry related calculator options
    """
    while True:
        choice = int(
            input(
                """(1) Find Area
(2) Find Circumference
(3) Find Perimeter
(4) Find Volume
(5) Return to list of calculators
(6) Exit

Which Geometry calculator would you like to use: """
            )
        )
        print()

        if choice == 1:
            choice = int(
                input(
                    """(1) Area of a Rectangle
(2) Area of a Circle

Which Shape would you like to solve the area for: """
                )
            )
            print()

            if choice == 1:
                length = float(
                    repeat_input(
                        "Length: ",
                        "Length must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                width = float(
                    repeat_input(
                        "Width: ",
                        "Width must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                print()
                area = length * width
                print(colors.green, "Area of a Rectangle:", area, colors.reset, "\n")
            elif choice == 2:
                radius = float(
                    repeat_input(
                        "Radius: ",
                        "Radius must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                print()
                area = math.pi * radius * radius
                print(colors.green, "Area of a Circle:", area, colors.reset, "\n")
            else:
                print(colors.red + "User input error found...\n", colors.reset)

        elif choice == 2:
            radius = float(
                repeat_input(
                    "Radius: ",
                    "Radius must be positive",
                    "float",
                    lambda i: float(i) >= 0,
                )
            )
            print()
            circumference = 2 * math.pi * radius
            print(colors.green, "Circumference:", circumference, colors.reset, "\n")

        elif choice == 3:
            a = float(
                repeat_input(
                    "Length: ",
                    "Length must be positive",
                    "float",
                    lambda i: float(i) >= 0,
                )
            )
            b = float(
                repeat_input(
                    "Width: ",
                    "Width must be positive",
                    "float",
                    lambda i: float(i) >= 0,
                )
            )
            c = float(
                repeat_input(
                    "Height: ",
                    "Height must be positive",
                    "float",
                    lambda i: float(i) >= 0,
                )
            )
            print()
            perimeter = a + b + c
            print(colors.green, "Perimeter:", perimeter, colors.reset, "\n")

        elif choice == 4:
            choice = int(
                input(
                    """(1) Volume of a Cube
(2) Volume of a Right Rectangular Prism
(3) Volume of a Cylinder

Which Shape would you like to solve the volume for: """
                )
            )
            print()

            if choice == 1:
                side = float(
                    repeat_input(
                        "Length: ",
                        "Length must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                print()
                volume = side**2 * side
                print(colors.green, "Volume:", volume, colors.reset, "\n")
            elif choice == 2:
                length = float(
                    repeat_input(
                        "Length: ",
                        "Length must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                width = float(
                    repeat_input(
                        "Width: ",
                        "Width must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                height = float(
                    repeat_input(
                        "Height: ",
                        "Height must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                print()
                volume = length * width * height
                print(colors.green, "Volume:", volume, colors.reset, "\n")
            elif choice == 3:
                area = float(
                    repeat_input(
                        "Radius: ",
                        "Radius must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                height = float(
                    repeat_input(
                        "Height: ",
                        "Height must be positive",
                        "float",
                        lambda i: float(i) >= 0,
                    )
                )
                print()
                volume = math.pi * area * area * height
                print(colors.green, "Volume:", volume, colors.reset, "\n")
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
    user_shares = float(
        repeat_input(
            "Number of Shares: ", "Must be positive", "float", lambda i: float(i) > 0
        )
    )
    user_purchase_price = float(
        repeat_input(
            "Purchase Price ($): ", "Must be positive", "float", lambda i: float(i) > 0
        )
    )
    user_sell_price = float(
        repeat_input(
            "Sell Price ($): ", "Must be positive", "float", lambda i: float(i) > 0
        )
    )
    user_buy_commission = float(
        repeat_input(
            "Buy Commission (if none, put 0): ",
            "Must be positive",
            "float",
            lambda i: float(i) >= 0,
        )
    )
    user_sell_commission = float(
        repeat_input(
            "Sell Commission (if none, put 0): ",
            "Must be positive",
            "float",
            lambda i: float(i) >= 0,
        )
    )
    print()
    results(
        user_shares,
        user_sell_commission,
        user_buy_commission,
        user_sell_price,
        user_purchase_price,
    )


def results(
    user_shares,
    user_sell_commission,
    user_buy_commission,
    user_sell_price,
    user_purchase_price,
):
    """
    Handles the main formula used to find gain/loss in the stocks function
    """
    user_gain_loss = ((user_sell_price * user_shares) - user_sell_commission) - (
        (user_purchase_price * user_shares) + user_buy_commission
    )

    print(
        colors.green + "Profit gain/loss:",
        user_gain_loss,
        "Dollars.",
        colors.reset,
        "\n",
    )


def random_number():
    """
    Basic function that returns a random integer between two sets of boundary integers, used in the randomization function
    """
    start_number = int(
        repeat_input("Pick a starting number: ", "Must be a number", "int")
    )
    end_number = int(repeat_input("Pick a ending number: ", "Must be a number", "int"))
    print()
    number = random.randint(start_number, end_number)
    print(colors.green, "Your random generated number:", number, "\n", colors.reset)


def heads_or_tails():
    """
    Small game of heads or tails used in the randomization function
    """
    choice = repeat_input(
        "Pick heads or tails: ",
        "Invalid choice",
        custom_validation=lambda i: i in ["heads", "h", "t", "tails", "tail", "head"],
    )

    coin_flip = ["heads", "tails"]
    print("You have picked:", choice)
    print("The coin flip landed on:", random.choice(coin_flip), "\n")


def random_erdos_graph():
    # Create a random Erdős-Rényi graph with 20 nodes and a probability of edge creation p=0.3
    G = nx.erdos_renyi_graph(20, 0.3)

    # Draw the graph
    nx.draw(G, with_labels=True, node_color="skyblue", node_size=500)
    plt.title("Random Erdős-Rényi Graph")
    plt.show()


def random__graph():
    # Create an empty graph
    G = nx.Graph()

    # Add nodes to the graph (you can specify the number of nodes)
    G.add_nodes_from([1, 2, 3, 4, 5])

    # Add random edges between nodes
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

    # Draw the graph
    nx.draw(
        G,
        with_labels=True,
        node_color="skyblue",
        node_size=500,
        font_size=12,
        font_color="black",
        font_weight="bold",
    )
    plt.title("Random Graph")
    plt.show()


def randomization():
    """
    Main hub for all randomization calculators/games
    """
    while True:
        choice = int(
            input(
                """(1) Random Number Generator
(2) Heads or Tails
(3) Generate a random Erdős-Rényi graph
(4) Generate a random graph
(5) Return to list of calculators
(6) Exit

Which calculation would you like to perform: """
            )
        )
        print()

        if choice == 1:
            random_number()
        elif choice == 2:
            heads_or_tails()
        elif choice == 3:
            random_erdos_graph()
        elif choice == 4:
            random__graph()
        elif choice == 5:
            break
        elif choice == 6:
            raise Exit
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)


def bitwise():
    """
    Turns the result from bin into something nice
    """
    bin_number = lambda x: bin_number(x)[2:] if x >= 0 else "-" + bin_number(x)[3:]
    binary_operators = {"&", "|", "^", "<<", ">>"}
    unary_operators = {"~"}

    operand_1 = int(repeat_input("First number: ", "Must be an integer", "int"))
    operator = repeat_input(
        "Operator (&, |, ^, <<, or >>): ",
        "Must be a bitwise operator",
        custom_validation=lambda i: i in binary_operators | unary_operators,
    )

    if operator in binary_operators:
        operand_2 = int(repeat_input("Second number: ", "Must be an integer", "int"))
        answer = eval(str(operand_1) + operator + str(operand_2))

        print(f"{operand_1} {operator} {operand_2} = {answer}")
        print(
            f"{bin_number(operand_1)} {operator} {bin_number(operand_2)} = {bin_number(answer)}"
        )
    else:
        answer = eval(operator + str(operand_1))

        print(f"{operator}{operand_1} = {answer}")
        print(f"{operator}{bin_number(operand_1)} = {bin_number(answer)}")


def gaming():
    """
    Main calculator used for everything gaming related
    """
    while True:
        choice = int(
            input(
                """(1) KD (Kill Death) ratio
(2) KDA (Kill Death Assist) ratio
(3) Win/Loss ratio
(4) Return to list of calculators
(5) Exit
    
Which option would you like to pick: """
            )
        )
        print()

        if choice == 1:
            kills = int(input("Total kills: "))
            print()
            deaths = int(input("Total deaths: "))
            print()
            kd = kills / deaths
            if kd == 1.0:
                print(
                    colors.yellow + "Your KD ratio is " + str(kd),
                    "This ratio is average in gaming.\n",
                    colors.reset,
                )
            elif kd < 1.0:
                print(
                    colors.red + "Your KD ratio is " + str(kd),
                    "This ratio is below average in gaming.\n",
                    colors.reset,
                )
            elif kd > 1.0:
                print(
                    colors.green + "Your KD ratio is " + str(kd),
                    "This ratio is above average in gaming.\n",
                    colors.reset,
                )
            else:
                print(colors.red + "User input error found...\n", colors.reset)
                time.sleep(2)
        elif choice == 2:
            kills = int(input("Total kills: "))
            print()
            deaths = int(input("Total deaths: "))
            print()
            assists = int(input("Total assists: "))
            print()
            kda = (kills + assists) / deaths
            if kda == 1.0:
                print(
                    colors.yellow + "Your KDA ratio is " + str(kda),
                    "This ratio is average in gaming.\n",
                    colors.reset,
                )
            elif kda < 1.0:
                print(
                    colors.red + "Your KDA ratio is " + str(kda),
                    "This ratio is below average in gaming.\n",
                    colors.reset,
                )
            elif kda > 1.0:
                print(
                    colors.green + "Your KDA ratio is " + str(kda),
                    "This ratio is above average in gaming.\n",
                    colors.reset,
                )
            else:
                print(colors.red + "User input error found...\n", colors.reset)
                time.sleep(2)
        elif choice == 3:
            wins = int(input("Total wins: "))
            print()
            loses = int(input("Total loses: "))
            print()
            win_loss_ratio = wins / loses
            if win_loss_ratio == 1.0:
                print(
                    colors.yellow + "Your Win/Loss ratio is " + str(win_loss_ratio),
                    "This ratio is average in gaming.\n",
                    colors.reset,
                )
            elif win_loss_ratio < 1.0:
                print(
                    colors.red + "Your Win/Loss ratio is " + str(win_loss_ratio),
                    "This ratio is below average in gaming.\n",
                    colors.reset,
                )
            elif win_loss_ratio > 1.0:
                print(
                    colors.green + "Your Win/Loss ratio is " + str(win_loss_ratio),
                    "This ratio is above average in gaming.\n",
                    colors.reset,
                )
            else:
                print(colors.red + "User input error found...\n", colors.reset)
                time.sleep(2)
        elif choice == 4:
            break
        elif choice == 5:
            raise Exit
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)


def download_time():
    """
    Used to calculate the download time for a file size being downloaded.
    """
    download_speed = float
    print(colors.yellow + "---Important notes about this calculator---\n")
    time.sleep(1)
    print(
        "Please keep in mind that the download time calculator will give you only an estimate of how long it will take to download something. Given that most peoples download speeds cannot be given a single value but rather an average, no estimate of download time can be 100 percent accurate. To provide the best accuracy with timing, we ask to give an average of your overall download speed.\n"
    )
    time.sleep(1)
    print(
        "If your download size is in Gigabytes, just convert that value to Megabytes. Every 1000 Mb equals a Gb, for example, if you have a download size of 23 Gb, then your download size would 23000 in Mb.\n",
        colors.reset,
    )
    time.sleep(1)
    file_size = int(
        input(
            """(1) Megabytes

Select which file size type the download is: """
        )
    )
    print()

    if file_size == 1:
        file_size = float(input("How many total megabytes is your download: "))
        print()
        print(
            colors.yellow
            + "If you are unsure what your average download/upload speeds are, please go to https://www.speedtest.net/ to find out more.\n",
            colors.reset,
        )
        time.sleep(1)
        download_speed = float(
            input("How many megabytes per second on average is your download speed: ")
        )
        print()
    else:
        print(colors.red + "User input error found...\n", colors.reset)
        time.sleep(2)
    print("Here's how long it will take for your download to complete...")
    download_time_in_seconds = file_size / (download_speed / 8)
    print(colors.green + str(download_time_in_seconds), "Seconds.")
    download_time_in_minutes = download_time_in_seconds / 60
    print(str(download_time_in_minutes), "Minutes.")
    download_time_in_hours = download_time_in_minutes / 60
    print(str(download_time_in_hours), "Hours.\n", colors.reset)


# Function to simulate a coin flip
def coin_flip():
    return random.choice(["Heads", "Tails"])


def conditional_probability():
    # Define the total sample space size (total number of possible outcomes)
    total_sample_space = float(input("Enter the size of the sample space: "))
    # Get the count of event A (e.g., the number of successful outcomes)
    event_a = float(input("Enter the count of event A: "))
    # Get the count of event B (e.g., the number of successful outcomes)
    event_b = float(input("Enter the count of event B: "))
    # Calculate the conditional probability and display the result
    # Calculate P(A ∩ B), the probability of both events A and B occurring
    p_a_and_b = event_a / total_sample_space
    # Calculate P(B), the probability of event B occurring
    p_b = event_b / total_sample_space
    # Calculate P(A|B), the conditional probability of A given B
    p_a_given_b = p_a_and_b / p_b
    print(p_a_given_b, "\n")


def probability():
    # Option to calculate probability or simulate coin flips
    choice = int(
        input(
            "Calculate the probability of something (1) or simulate the probability of coin flips (2) or odds of winning the lottery (3) or find a conditional probability (4): "
        )
    )

    if choice == 1:
        # Get user input for total outcomes and successful outcomes
        while True:
            try:
                total_outcomes = int(
                    input("Enter the total number of possible outcomes: ")
                )
                successful_outcomes = int(
                    input("Enter the number of successful outcomes: ")
                )
                if (
                    total_outcomes > 0
                    and successful_outcomes >= 0
                    and successful_outcomes <= total_outcomes
                ):
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
                num_flips = int(
                    input(
                        "Number of coin flips (higher numbers result in longer waiting times): "
                    )
                )
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

    elif choice == 3:
        lottery()

    elif choice == 4:
        conditional_probability()

    else:
        print("Invalid choice. Please select 1 or 2.\n")


def gpa():
    num_courses = int(input("Enter the number of courses: "))

    grades = []
    credits = []

    for i in range(num_courses):
        course_grade = float(input(f"Enter the grade for course {i + 1} (0-4.0): "))
        course_credit = float(input(f"Enter the credit hours for course {i + 1}: "))

        grades.append(course_grade)
        credits.append(course_credit)

    total_credits = sum(credits)
    weighted_grade_points = sum(
        grade * credit for grade, credit in zip(grades, credits)
    )
    gpa = weighted_grade_points / total_credits
    print(f"Your GPA is: {gpa:.2f}\n")


def financial_aid():
    # Get user input for family income, household size, and cost of attendance
    family_income = float(input("Enter family income: "))
    household_size = int(input("Enter household size: "))
    cost_of_attendance = float(input("Enter cost of attendance: "))

    # Perform eligibility calculation (example criteria)
    if family_income < 50000 and household_size <= 4 and cost_of_attendance > 0:
        eligible = True
    else:
        eligible = False

    if eligible:
        print("You are eligible for financial aid.\n")
    else:
        print("You are not eligible for financial aid.\n")


def Student_Teacher_Ratio():
    # Get user input for the number of students and the number of teachers
    num_students = int(input("Enter the number of students: "))
    num_teachers = int(input("Enter the number of teachers: "))

    # Calculate student-to-teacher ratio
    student_teacher_ratio = num_students / num_teachers

    print(f"Student-to-Teacher Ratio: {student_teacher_ratio}\n")


def Graduation_Rate():
    # Get user input for the number of students who graduated and the total number of students at the beginning
    graduated_students = int(input("Enter the number of students who graduated: "))
    initial_students = int(input("Enter the number of students at the beginning: "))

    # Calculate graduation rate
    graduation_rate = (graduated_students / initial_students) * 100

    print(f"Graduation Rate: {graduation_rate}%\n")


def Dropout_Rate():
    # Get user input for the number of students who dropped out and the total number of students at the beginning
    dropout_students = int(input("Enter the number of students who dropped out: "))
    initial_students = int(input("Enter the number of students at the beginning: "))

    # Calculate dropout rate
    dropout_rate = (dropout_students / initial_students) * 100

    print(f"Dropout Rate: {dropout_rate}%\n")


def Retention_Rate():
    # Get user input for the number of students at the beginning and end of a period
    initial_students = int(input("Enter the number of students at the beginning: "))
    final_students = int(input("Enter the number of students at the end: "))

    # Calculate retention rate
    retention_rate = (final_students / initial_students) * 100

    print(f"Retention Rate: {retention_rate}%\n")


def Attendance_Rate():
    # Get user input for the number of classes attended and the total number of classes
    classes_attended = int(input("Enter the number of classes attended: "))
    total_classes = int(input("Enter the total number of classes: "))

    # Calculate attendance rate
    attendance_rate = (classes_attended / total_classes) * 100

    print(f"Attendance Rate: {attendance_rate}%\n")


def Percentage_Scores():
    # Get user input for marks obtained and total marks
    marks_obtained = float(input("Enter marks obtained: "))
    total_marks = float(input("Enter total marks: "))

    # Calculate the percentage
    percentage = (marks_obtained / total_marks) * 100

    print(f"Percentage: {percentage}%\n")


education_functions = {
    1: gpa,
    2: Percentage_Scores,
    3: Attendance_Rate,
    4: Retention_Rate,
    5: Dropout_Rate,
    6: Graduation_Rate,
    7: Student_Teacher_Ratio,
    8: financial_aid,
}


def education():
    choice = input(
        """(1) GPA (Grade Point Average)
(2) Percentage Scores
(3) Attendance Rate
(4) Retention Rate
(5) Dropout Rate
(6) Graduation Rate
(7) Student-to-Teacher Ratio
(8) Financial Aid Eligibility
(9) Return
Choose an education calculator: """
    )
    print("")

    if choice.lower() == "exit":
        print("Exiting the Ultimate Calculator...")
        quit()

    try:
        choice = int(choice)
        if choice in education_functions:
            education_functions[choice]()  # Call the selected education function
        elif choice == 9:
            return
        else:
            print(
                colors.red
                + 'Invalid choice. Please select a valid calculator or "exit".\n',
                colors.reset,
            )
    except ValueError:
        print(
            colors.red
            + 'Invalid input. Please enter a valid integer choice or "exit".\n',
            colors.reset,
        )


def lottery():
    # Define the parameters of the lottery game
    num_tickets = 1000000  # Number of tickets purchased
    winning_numbers = [random.randint(1, 20) for _ in range(5)]

    # Initialize a counter to keep track of the number of wins
    num_wins = 0

    # Simulate the lottery draws
    for _ in range(1):
        for _ in range(num_tickets):
            ticket = [random.randint(1, 20) for _ in range(5)]

            # Check if the ticket matches the winning numbers
            if ticket == winning_numbers:
                num_wins += 1

    # Calculate the probability of winning
    probability = num_wins / num_tickets

    print(f"Winning Numbers: {winning_numbers}")
    print(f"Number of Wins: {num_wins}")
    print(f"Number of Tickets Purchased: {num_tickets}")
    print(f"Probability of Winning: {probability:.6f}\n")


def start():
    calculator_functions = {
        1: basic_calc,
        2: algebra,
        3: geometry,
        4: financial,
        5: health,
        6: randomization,
        7: stocks,
        8: bitwise,
        9: percentage,
        10: gaming,
        11: download_time,
        12: probability,
        13: education,
        14: stats,
    }

    while True:
        print(colors.green + "All Calculators", colors.reset)
        print(
            """
(1) Basic Calculator
(2) Algebra
(3) Geometry
(4) Financial
(5) Health
(6) Randomization
(7) Stocks
(8) Bitwise Operations
(9) Percentage
(10) Gaming
(11) Download Time
(12) Probability
(13) Education
(14) Statistics
(15) Main Menu
        """
        )
        choice = input("Which calculator would you like to use (or 'exit' to quit): ")
        print("")

        if choice.lower() == "exit":
            print("Exiting the Ultimate Calculator...")
            quit()
        try:
            choice = int(choice)
            if choice in calculator_functions:
                calculator_functions[choice]()
            elif choice == 15:
                return
            else:
                print(
                    colors.red
                    + 'Invalid choice. Please select a valid calculator or "exit".\n',
                    colors.reset,
                )
        except ValueError:
            print(
                colors.red
                + 'Invalid input. Please enter a valid integer choice or "exit".\n',
                colors.reset,
            )


if __name__ == "__main__":
    start()
