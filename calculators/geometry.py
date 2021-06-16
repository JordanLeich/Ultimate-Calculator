import math
import time
import colors
import restart


def start():
    choice = int(input('''(1) Find Area
(2) Find Circumference
(3) Find Perimeter
(4) Find Volume

Which Geometry calculator would you like to use: '''))
    print()

    if choice == 1:
        choice = int(input('''(1) Area of a Rectangle
(2) Area of a Circle

Which Shape would you like to solve the area for: '''))
        print()

        if choice == 1:
            length = float(input('Length: '))
            width = float(input('Width: '))
            print()
            area = length * width
            print(colors.green, "Area of a Rectangle:", area, colors.reset, '\n')
            restart.restart()
        elif choice == 2:
            radius = float(input('Radius: '))
            print()
            area = math.pi * radius * radius
            print(colors.green, "Area of a Circle:", area, colors.reset, '\n')
            restart.restart()
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)
            start()
    elif choice == 2:
        radius = float(input('Radius: '))
        print()
        circumference = 2 * math.pi * radius
        print(colors.green, "Circumference:", circumference, colors.reset, '\n')
        restart.restart()
    elif choice == 3:
        a = float(input('A: '))
        b = float(input('B: '))
        c = float(input('C: '))
        print()
        perimeter = a + b + c
        print(colors.green, "Perimeter:", perimeter, colors.reset, '\n')
        restart.restart()
    elif choice == 4:
        choice = int(input('''(1) Volume of a Cube
(2) Volume of a Right Rectangular Prism
(3) Volume of a Prism or Cylinder

Which Shape would you like to solve the volume for: '''))
        print()

        if choice == 1:
            side = float(input('Length of the Side: '))
            print()
            volume = side * side * side
            print(colors.green, "Volume:", volume, colors.reset, '\n')
            restart.restart()
        elif choice == 2:
            length = float(input('Length: '))
            width = float(input('Width: '))
            height = float(input('Height: '))
            print()
            volume = length * width * height
            print(colors.green, "Volume:", volume, colors.reset, '\n')
            restart.restart()
        elif choice == 3:
            area = float(input('Area / Base / Radius: '))
            height = float(input('Height: '))
            print()
            volume = math.pi * area * area * height
            print(colors.green, "Volume:", volume, colors.reset, '\n')
            restart.restart()
        else:
            print(colors.red + "User input error found...\n", colors.reset)
            time.sleep(2)
            start()

    else:
        print(colors.red + "User input error found...\n", colors.reset)
        time.sleep(2)
        start()


if __name__ == '__main__':
    start()
