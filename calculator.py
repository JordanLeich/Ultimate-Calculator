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
    number1 = float(input("What is your first number: "))
    print()
    number2 = float(input("What is your second number: "))
    print()
    operator1 = str(
        input('Choose an operator (+, -, *, /, or ** to multiply by a power) '))
    print()

    if operator1.lower() == "+" or operator1.lower() == "add":
        print(colors.green, addition(number1, number2), colors.reset, '\n')
        restart.restart()

    elif operator1.lower() == "-" or operator1.lower() == "subtract":
        print(colors.green, subtract(number1, number2), colors.reset, '\n')
        restart.restart()

    elif operator1.lower() == "*" or operator1.lower() == "multiply" or operator1.lower() == "times":
        print(colors.green, multiply(number1, number2), colors.reset, '\n')
        restart.restart()

    elif number1 == 0 or number2 == 0 and operator1.lower() == "/" or operator1.lower() == "divide":
        print(ZeroDivisionError)
        print(colors.red + "You cannot divide by zero!\n", colors.reset)
        restart.restart()

    elif operator1.lower() == "/" or operator1.lower() == "divide" or operator1.lower() == "division":
        print(colors.green, divide(number1, number2), colors.reset, '\n')
        restart.restart()

    elif operator1.lower() == "**" or operator1.lower() == 'power':
        print(colors.green, power(number1, number2), colors.reset, '\n')
        restart.restart()

    else:
        print(colors.red + 'Operation error found!\n', colors.reset)
        restart.restart()


if __name__ == '__main__':
    start()
