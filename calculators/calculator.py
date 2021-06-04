# Imports
import time
import colors
import restart

# Variables
operator = float
result = float
number1 = float
number2 = float


# Entire operation
def start():
    global operator, result, number1, number2

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
    operator = input('Choose an operator (+, -, *, /, or ** to multiply by a power) ')
    print()

    # Keep asking the user until they enter a valid operator
    while operator not in operator_options:
        print("Invalid Operator, Please Choose Again.")
        operator = input('Choose an operator (+, -, *, /, or ** to multiply by a power) ')
    print()

    # "in []" is better with multiple choices
    if operator.lower() in ["+", "add"]:
        addition = number1 + number2
        print(colors.green, addition, colors.reset, '\n')

    elif operator.lower() in ["-", "subtract"]:
        subtract = number1 - number2
        print(colors.green, subtract, colors.reset, '\n')

    elif operator.lower() in ["*", "multiply", "times"]:
        multiply = number1 * number2
        print(colors.green, multiply, colors.reset, '\n')

    elif operator.lower() in ["/", "divide", "division"]:
        if 0 in [number1, number2]:
            print(colors.red + "You cannot divide by zero!\n", colors.reset)
        else:
            divide = number1 / number2
            print(colors.green, divide, colors.reset, '\n')

    elif operator.lower() in ["**", "power"]:
        power = number1 ** number2
        print(colors.green, power, colors.reset, '\n')

    # it's kinda annoying to restart after, so I added continue option
    # change the variable names because I'm not really good with naming variables
    input_1 = str(input("Would you like to make another arithmetic calculation (yes / no): "))

    if input_1.lower() == "yes" or input_1.lower() == 'y':
        start()
    elif input_1.lower() == "no" or input_1.lower() == 'n':
        restart.restart()
    else:
        print(colors.red+'User input error found...')
        time.sleep(2)
        restart.restart()


if __name__ == '__main__':
    start()
