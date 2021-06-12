import math
import colors
import end
import restart
from math import sqrt
from tools import repeat_input


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
        side_a = sqrt((side_c * side_c) - (side_b * side_b))

        return side_a

    elif formula == 'b':
        side_a = int(a)
        side_c = int(c)
        side_b = sqrt(side_c * side_c - side_a * side_a)

        return side_b

    elif formula == 'c':
        side_a = int(a)
        side_b = int(b)
        side_c = sqrt(side_a * side_a + side_b * side_b)

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


def start():
    choice = int(input('''
(1) Find Slope (Rise Over Run)
(2) Find Slope Intercept (y=mx+b)
(3) Find Pythagorean Theorem
(4) Find The Distance Between Two Points
(5) Find The Midpoint of a Line
(6) Restart
(7) Quit
What calculation would you like to perform: '''))
    print()

    if choice == 1:
        float_error = "Invalid Number...\n"
        y2 = repeat_input("What is your Y2 value: ", float_error, "float")
        y1 = repeat_input("What is your Y1 value: ", float_error, "float")
        x2 = repeat_input("What is your X2 value: ", float_error, "float")
        x1 = repeat_input("What is your X1 value: ", float_error, "float")

        result = find_slope1(y2, y1, x2, x1)
        print(colors.green + 'Slope:', result, '\n', colors.reset)
        restart.restart()

    elif choice == 2:
        m = repeat_input('What is your M value: ', "Invalid Number...\n", "float")
        x = repeat_input('What is your X value: ', "Invalid Number...\n", "float")
        b = repeat_input('What is your B value: ', "Invalid Number...\n", "float")

        result = find_slope2(m, x, b)
        print(colors.green + 'Result:', result, '\n', colors.reset)
        restart.restart()

    elif choice == 3:
        while True:
            formula = input('Which side (a, b, c) do you wish to calculate: ')
            if formula in ['a', 'b', 'c']:
                break
            print(colors.red + 'User input error found...\n', colors.reset)

        if formula.lower() == 'a':
            b = repeat_input('Input the length of side b: ', "Invalid Number...\n", 'float')
            c = repeat_input('Input the length of side c: ', "Invalid Number...\n", 'float')

            result = find_pythagorean(formula, b=b, c=c)
            print(colors.green + 'The length of side a is:', result, '\n', colors.reset)
            restart.restart()

        elif formula.lower() == 'b':
            a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
            c = repeat_input('Input the length of side c: ', "Invalid Number...\n", 'float')

            result = find_pythagorean(formula, a=a, c=c)
            print(colors.green + 'The length of side b is:', result, '\n', colors.reset)
            restart.restart()

        elif formula.lower() == 'c':
            a = repeat_input('Input the length of side a: ', "Invalid Number...\n", 'float')
            b = repeat_input('Input the length of side b: ', "Invalid Number...\n", 'float')

            result = find_pythagorean(formula, a=a, b=b)
            print(colors.green + 'The length of side c is:', result, '\n', colors.reset)
            restart.restart()

    elif choice == 4:
        x1 = repeat_input('x1 Value: ', "Invalid Number...\n", "float")
        y1 = repeat_input('y1 Value: ', "Invalid Number...\n", "float")
        x2 = repeat_input('x2 Value: ', "Invalid Number...\n", "float")
        y2 = repeat_input('y2 Value: ', "Invalid Number...\n", "float")

        distance = find_distance(x1, y1, x2, y2)
        print(colors.green + "The distance between the two points is", distance, '\n', colors.reset)
        restart.restart()

    elif choice == 5:
        x1 = repeat_input('The value of x1: ', "Invalid Number...\n", "float")
        y1 = repeat_input('The value of y1: ', "Invalid Number...\n", "float")
        x2 = repeat_input('The value of x2: ', "Invalid Number...\n", "float")
        y2 = repeat_input('The value of y2: ', "Invalid Number...\n", "float")

        midpoint = find_midpoint(x1, y1, x2, y2)
        x_m_point = midpoint[0]
        y_m_point = midpoint[1]

        print(colors.green + "The midpoint's x value is: ", x_m_point)
        print("The midpoint's y value is: ", y_m_point, '\n', colors.reset)
        restart.restart()

    elif choice == 6:
        restart.restart()

    elif choice == 7:
        end.end()

    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        start()


if __name__ == '__main__':
    start()
