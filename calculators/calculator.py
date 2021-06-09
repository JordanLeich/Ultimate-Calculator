import time
import colors
import restart


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
                print(colors.red+"Error Found...\n", colors.reset)
                continue

        if operator == "=":
            print()
            print(colors.green + " ".join(calculation), calculator(calculation), colors.reset)
            break
        print(" ".join(calculation))

    # Better Variable Names :)
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


if __name__ == '__main__':
    start()
