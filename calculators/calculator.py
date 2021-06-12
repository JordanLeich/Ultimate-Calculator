import colors
import restart
from tools import repeat_input


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
def start():
    print(colors.yellow + 'When you are finishing making your arithmetic problem, please use = when asked for an '
                          'operator!\n', colors.reset)
    calculation = []
    while True:
        number = repeat_input("Your Number: ", "Invalid Number...\n", "float")
        calculation.append(number)

        operator = repeat_input("Your Operator: ", "Invalid Operator...\n", "operator")
        calculation.append(operator)

        if operator == "=":
            print()
            print(colors.green + " ".join(calculation), calculator(calculation), colors.reset)
            break

        print(" ".join(calculation))

    print()
    continue_text = "Would you like to make another arithmetic calculation (yes / no): "
    continue_opt = repeat_input(continue_text, "User input error found...\n", "yes_no")
    if continue_opt.lower() in ['y', 'yes']:
        start()
    elif continue_opt.lower() in ['n', 'no']:
        restart.restart()


if __name__ == '__main__':
    start()
