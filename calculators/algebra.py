import math
import colors
import end
import restart
from math import sqrt


def start():
    choice = int(input('''
(1) Find Slope (Rise Over Run)
(2) Find Slope Intercept (y=mx+b)
(3) Find Pythagorean Theorem
(4) Find The Distance Between Two Points
(5) Find The Midpoint
(6) Restart
(7) Quit
What calculation would you like to perform: '''))
    print()

    if choice == 1:
        y2 = float(input('What is your Y2 value: '))
        y1 = float(input('What is your Y1 value: '))
        x2 = float(input('What is your X2 value: '))
        x1 = float(input('What is your X1 value: '))
        slope = (y2 - y1) / (x2 - x1)
        print()
        print(colors.green + 'Slope:', slope, '\n', colors.reset)
        restart.restart()
    elif choice == 2:
        m = float(input('What is your M value: '))
        x = float(input('What is your X value (if x doesnt have a value, please type 1): '))
        b = float(input('What is your B value: '))
        y = m * x + b
        print()
        print(colors.green + 'Result:', y, '\n', colors.reset)
        restart.restart()
    elif choice == 3:
        formula = input('Which side (a, b, c) do you wish to calculate: ')

        if formula == 'c':
            side_a = int(input('Input the length of side a: '))
            side_b = int(input('Input the length of side b: '))
            side_c = sqrt(side_a * side_a + side_b * side_b)
            print()
            print(colors.green + 'The length of side c is:', side_c, '\n', colors.reset)
            restart.restart()
        elif formula == 'a':
            side_b = int(input('Input the length of side b: '))
            side_c = int(input('Input the length of side c: '))
            side_a = sqrt((side_c * side_c) - (side_b * side_b))
            print()
            print(colors.green + 'The length of side a is', side_a, '\n', colors.reset)
            restart.restart()
        elif formula == 'b':
            side_a = int(input('Input the length of side a: '))
            side_c = int(input('Input the length of side c: '))
            side_b = sqrt(side_c * side_c - side_a * side_a)
            print(colors.green + 'The length of side b is', side_b, '\n', colors.reset)
            restart.restart()
        else:
            print('Select a side between either a, b, or c.\n')
            restart.restart()
    elif choice == 4:
        x1 = float(input('x1 Value: '))
        y1 = float(input('y1 Value: '))
        x2 = float(input('x2 Value: '))
        y2 = float(input('y2 Value: '))
        print()
        distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        print(colors.green + "The distance between the two points is", distance, '\n', colors.reset)
        restart.restart()
    elif choice == 5:
        x1 = float(input('The value of x1: '))
        y1 = float(input('The value of y1: '))
        x2 = float(input('The value of x2: '))
        y2 = float(input('The value of y2: '))
        print()
        x_m_point = (x1 + x2) / 2
        y_m_point = (y1 + y2) / 2
        print(colors.green+"The midpoint's x value is: ", x_m_point)
        print("The midpoint's y value is: ", y_m_point, '\n', colors.reset)
        restart.restart()
    elif choice == 6:
        restart.restart()
    elif choice == 7:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        start()
