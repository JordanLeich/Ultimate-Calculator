# Imports
import colors
import restart

# Variables
pi = 3.14
operator1 = float
result = float


def addition(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def power(number1, number2):
    return number1 ** number2


def divide(number1, number2):
    return number1 / number2


# Entire operation
def start():
    global operator1, result

    # Keep asking the user until they enter a valid input
    while True:
        try:
            number1 = float(input("What is your first number: "))
            print()
            break
        except ValueError:
            print("Invalid Input.")
            continue

    while True:
        try:
            number2 = float(input("What is your second number: "))
            print()
            break
        except ValueError:
            print("Invalid Input.")
            continue

    operator_options = ["+", "-", "*", "/", "**",
                        "add", "subtract", "multiply",
                        "times", "divide", "division", "power"]
    # input() is already a str by default
    operator1 = input('Choose an operator (+, -, *, /, or ** to multiply by a power) ')
    print()

    # Keep asking the user until they enter a valid operator
    while operator1 not in operator_options:
        print("Invalid Operator, Please Choose Again.")
        operator1 = input('Choose an operator (+, -, *, /, or ** to multiply by a power) ')
    print()

    # "in []" is better with multiple choices
    if operator1.lower() in ["+", "add"]:
        print(colors.green, addition(number1, number2), colors.reset, '\n')

    elif operator1.lower() in ["-", "subtract"]:
        print(colors.green, subtract(number1, number2), colors.reset, '\n')

    elif operator1.lower() in ["*", "multiply", "times"]:
        print(colors.green, multiply(number1, number2), colors.reset, '\n')

    elif operator1.lower() in ["/", "divide", "division"]:
        if 0 in [number1, number2]:
            print(colors.red + "You cannot divide by zero!\n", colors.reset)
        else:
            print(colors.green, divide(number1, number2), colors.reset, '\n')

    elif operator1.lower() in ["**", "power"]:
        print(colors.green, power(number1, number2), colors.reset, '\n')

    # it's kinda annoying to restart after, so I added continue option
    # change the variable names because I'm not really good with naming variables
    input_1 = input("Would you like to continue? Yes | No: ")
    while input_1.lower() not in ["yes", "no"]:
        input_1 = input("Would you like to continue? Yes | No: ")

    if input_1.lower() == "yes":
        start()
    else:
        restart.restart()


if __name__ == '__main__':
    start()
