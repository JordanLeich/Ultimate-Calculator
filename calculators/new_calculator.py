import time
import colors
import restart


def calculator(data):
    total = 0
    for ind, dta in enumerate(data):
        if dta == "+":
            total += int(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "-":
            total -= int(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "/":
            total /= int(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "*":
            total *= int(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "**":
            total **= int(data[ind + 1])
            data.pop(ind + 1)

        elif dta == "=":
            break

        else:
            total += int(dta)

    return total


# Entire operation
def start():
    calculation = []
    while True:
        number = input("Your Number: ")
        operator = input("Your Operator: ")
        calculation.append(number)
        calculation.append(operator)
        if operator == "=":
            print(" ".join(calculation), calculator(calculation))
            break
        print(" ".join(calculation))

    # Better Variable Names :)
    continue_opt = input("Would you like to make another arithmetic calculation (yes / no): ")
    if continue_opt.lower() in ['y', 'yes']:
        start()
    elif continue_opt.lower() in ['n', 'no']:
        restart.restart()
    else:
        print(colors.red + 'User input error found...')
        time.sleep(2)
        restart.restart()


if __name__ == '__main__':
    start()
