import colors
import end
import restart


def start():
    choice = int(input('''
(1) Find Slope (Rise Over Run)
(2) Find Slope Intercept (y=mx+b)
(3) Restart
(4) Quit
What calculation would you like to perform: '''))

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
        y = float(input('What is your Y value: '))
        m = float(input('What is your M value: '))
        x = float(input('What is your X value (if x doesnt have a value, please type 1): '))
        b = float(input('What is your B value: '))
        y = m(x)+b
        print()
        print(colors.green + 'Result:', y, '\n', colors.reset)
        restart.restart()
    elif choice == 3:
        restart.restart()
    elif choice == 4:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        start()
