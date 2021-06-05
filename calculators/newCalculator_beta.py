import time
import colors
import restart

# Variables
operator = float
result = float
number1 = float
number2 = float


def calculator(data):
    total = 0
    for ind, dta in enumerate(data):
        if dta == "+":
            total += int(data[ind + 1])
            data.pop(ind + 1)
        elif dta == "=":
            break
        else:
            total += int(dta)
    return total


# Entire operation
def start():
    global operator, result, number1, number2

    # Keep asking the user until they enter a valid input
    while True:
        calculation = []
        number = input("Your Number: ")
        operator = input("Your Operator: ")
        calculation.append(number)
        calculation.append(operator)
        if operator == "=":
            print(" ".join(calculation), calculator(calculation))
            break
        print(" ".join(calculation))

    # it's kinda annoying to restart after, so I added continue option
    # change the variable names because I'm not really good with naming variables
    input_1 = str(input("Would you like to make another arithmetic calculation (yes / no): "))

    if input_1.lower() == "yes" or input_1.lower() == 'y':
        start()
    elif input_1.lower() == "no" or input_1.lower() == 'n':
        restart.restart()
    else:
        print(colors.red + 'User input error found...')
        time.sleep(2)
        restart.restart()


if __name__ == '__main__':
    start()